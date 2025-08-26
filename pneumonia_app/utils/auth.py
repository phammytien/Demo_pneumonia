import streamlit as st
from utils.db_utils import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from mysql.connector import Error
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads/"
DEFAULT_AVATAR = "default_avatar.png"

def ensure_admin_exists():
    """Đảm bảo luôn có tài khoản admin mặc định"""
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id FROM users WHERE username='admin'")
        row = cursor.fetchone()
        if not row:
            hashed = generate_password_hash("admin123")
            cursor.execute("""
                INSERT INTO users (username, password, role, full_name, email, avatar, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, ("admin", hashed, "admin", "Quản trị viên", "admin@example.com", DEFAULT_AVATAR, "active"))
            conn.commit()
            print("✅ Tài khoản admin mặc định đã được tạo.")
    except Error as e:
        print(f"❌ Lỗi khi tạo admin mặc định: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def register(username, password, status="active"):
    """FIXED: Thêm status parameter với default='active'"""
    conn = get_connection()
    if not conn:
        st.error("Không kết nối được tới DB!")
        return False
    try:
        cursor = conn.cursor()
        hashed = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO users (username, password, status) 
            VALUES (%s, %s, %s)
        """, (username, hashed, status))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Tạo tài khoản thành công!")
        return True
    except Error as e:
        st.error(f"Lỗi khi đăng ký: {e}")
        return False

def login(username, password):
    """FIXED: Đăng nhập, trả về dict thông tin người dùng bao gồm STATUS nếu thành công"""
    ensure_admin_exists()
        
    conn = get_connection()
    if not conn:
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        # FIXED: Thêm field 'status' vào SELECT query
        cursor.execute("""
            SELECT id, username, password, role, full_name, email, phone, address, avatar, created_at, status
            FROM users WHERE username=%s
        """, (username,))
        row = cursor.fetchone()
        if row and check_password_hash(row["password"], password):
            del row["password"]
            # Lưu thông tin user vào session
            st.session_state["user"] = row
            return row
        return None
    except Error as e:
        st.error(f"Lỗi khi đăng nhập: {e}")
        return None
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# ========== CÁC HÀM MỚI CHO TÍNH NĂNG QUÊN MẬT KHẨU ==========

def check_username_exists(username):
    """Kiểm tra username có tồn tại trong database không"""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        return result is not None
    except Error as e:
        print(f"❌ Lỗi khi kiểm tra username: {e}")
        return False
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def get_user_email(username):
    """Lấy email của user để gửi mã xác thực"""
    conn = get_connection()
    if not conn:
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT email FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        return result['email'] if result else None
    except Error as e:
        print(f"❌ Lỗi khi lấy email: {e}")
        return None
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def reset_password_in_db(username, new_password):
    """Cập nhật mật khẩu mới trong database"""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        # Hash mật khẩu mới
        hashed_password = generate_password_hash(new_password)
        
        # Cập nhật mật khẩu trong database (bỏ updated_at vì cột không tồn tại)
        cursor.execute("""
            UPDATE users 
            SET password = %s
            WHERE username = %s
        """, (hashed_password, username))
        
        conn.commit()
        
        # Kiểm tra xem có cập nhật thành công không
        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật mật khẩu cho user: {username}")
            return True
        else:
            print(f"❌ Không tìm thấy user: {username}")
            return False
            
    except Error as e:
        print(f"❌ Lỗi khi cập nhật mật khẩu: {e}")
        return False
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def update_user_profile(user_id, full_name=None, email=None, phone=None, address=None):
    """Cập nhật thông tin profile của user"""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        
        # Tạo câu lệnh SQL động dựa trên các field được cập nhật
        update_fields = []
        values = []
        
        if full_name is not None:
            update_fields.append("full_name = %s")
            values.append(full_name)
        if email is not None:
            update_fields.append("email = %s")
            values.append(email)
        if phone is not None:
            update_fields.append("phone = %s")
            values.append(phone)
        if address is not None:
            update_fields.append("address = %s")
            values.append(address)
        
        if not update_fields:
            return True  # Không có gì để cập nhật
        
        # Thêm user_id vào values
        values.append(user_id)
        
        sql = f"UPDATE users SET {', '.join(update_fields)} WHERE id = %s"
        cursor.execute(sql, values)
        conn.commit()
        
        return cursor.rowcount > 0
        
    except Error as e:
        print(f"❌ Lỗi khi cập nhật profile: {e}")
        return False
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def change_password(username, old_password, new_password):
    """Đổi mật khẩu (yêu cầu mật khẩu cũ)"""
    conn = get_connection()
    if not conn:
        return False, "Không kết nối được database"
    
    try:
        cursor = conn.cursor(dictionary=True)
        
        # Kiểm tra mật khẩu cũ
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        
        if not result:
            return False, "Không tìm thấy tài khoản"
        
        if not check_password_hash(result['password'], old_password):
            return False, "Mật khẩu cũ không đúng"
        
        # Cập nhật mật khẩu mới (bỏ updated_at)
        hashed_password = generate_password_hash(new_password)
        cursor.execute("""
            UPDATE users 
            SET password = %s
            WHERE username = %s
        """, (hashed_password, username))
        
        conn.commit()
        return True, "Đổi mật khẩu thành công"
        
    except Error as e:
        return False, f"Lỗi database: {e}"
    finally:
        if cursor: cursor.close()
        if conn: conn.close()