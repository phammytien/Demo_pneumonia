import mysql.connector
from mysql.connector import Error

# Hàm tạo kết nối
def get_connection():
    try:
        conn = mysql.connector.connect(
            host="cabOOSE.proxy.rlwy.net",   # host Railway
            port=47488,                      # port Railway
            database="railway",              # tên database
            user="root",                     # user
            password="htlpYrDeHTlriVTkLHdMQPlbVdmQpqBQ"  # password Railway
        )
        if conn.is_connected():
            print("✅ Đã kết nối MySQL Railway thành công!")
            return conn
    except Error as e:
        print("❌ Lỗi khi kết nối MySQL Railway:", e)
        return None

# Hàm đóng kết nối
def close_connection(conn):
    if conn and conn.is_connected():
        conn.close()
        print("🔌 Đã đóng kết nối MySQL Railway.")

# ===================== LOG HOẠT ĐỘNG =====================
def add_log(user_id, action, details=""):
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO activity_logs (user_id, action, details) 
            VALUES (%s, %s, %s)
            """,
            (user_id, action, details)
        )
        conn.commit()
        cursor.close()
        close_connection(conn)
        print(f"📝 Log đã ghi: {action} - {details}")
    except Error as e:
        print("❌ Lỗi khi ghi log:", e)
