import streamlit as st
# from utils.auth import login, register
import random
import string
import time
from utils.auth import login, register, check_username_exists, get_user_email, reset_password_in_db



st.set_page_config(
    page_title="Hệ thống Chẩn đoán Bệnh Phổi", 
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS với màu xanh nhạt/đậm và nền trắng
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-blue: #2E86AB;
        --light-blue: #A5C3D9; 
        --lighter-blue: #E8F4F8;
        --dark-blue: #1B5E7F;
        --white: #FFFFFF;
        --light-gray: #F8FAFB;
        --text-dark: #2C3E50;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, var(--primary-blue) 0%, var(--dark-blue) 100%);
    }
    
    .css-17eq0hr {
        background: transparent;
        color: white;
    }
    
    .css-pkbazv {
        color: white !important;
        font-weight: 600;
    }
    
    /* Main content area */
    .main .block-container {
        background: var(--white);
        padding: 1rem 2rem;
        max-width: 1200px;
    }
    
    /* Header styling - COMPACT VERSION */
    .main-header {
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--light-blue) 100%);
        padding: 1.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 20px rgba(46, 134, 171, 0.25);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    
    .main-header h1 {
        font-size: 1.8rem;
        margin-bottom: 0.3rem;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        position: relative;
        z-index: 2;
    }
    
    .main-header p {
        font-size: 1rem;
        opacity: 0.95;
        position: relative;
        z-index: 2;
        margin: 0;
    }
    
    /* Feature cards */
    .feature-card {
        background: var(--white);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(46, 134, 171, 0.15);
        margin: 1rem 0;
        border: 1px solid var(--lighter-blue);
        border-left: 6px solid var(--primary-blue);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-blue), var(--light-blue));
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(46, 134, 171, 0.25);
    }
    
    .feature-card h4 {
        color: var(--primary-blue);
        margin-bottom: 1rem;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    .feature-card p {
        color: var(--text-dark);
        line-height: 1.6;
        margin-bottom: 0.5rem;
    }
    
    /* Stats cards */
    .stats-card {
        background: linear-gradient(135deg, var(--lighter-blue) 0%, var(--light-blue) 100%);
        padding: 2rem 1rem;
        border-radius: 16px;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(46, 134, 171, 0.2);
        transition: transform 0.3s ease;
        border: 1px solid rgba(46, 134, 171, 0.1);
    }
    
    .stats-card:hover {
        transform: scale(1.02);
    }
    
    .stats-card h3 {
        color: var(--dark-blue);
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stats-card p {
        color: var(--primary-blue);
        font-weight: 600;
        font-size: 0.95rem;
    }
    
    /* Login container - COMPACT VERSION */
    .login-container {
        background: var(--white);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 6px 25px rgba(46, 134, 171, 0.15);
        border: 1px solid var(--lighter-blue);
        max-width: 380px;
        margin: 1rem auto;
    }
    
    .login-container h4 {
        color: var(--primary-blue);
        text-align: center;
        margin-bottom: 1.2rem;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    /* Compact form styling */
    .compact-form {
        margin: 0.8rem 0;
    }
    
    .compact-form .stTextInput > div > div > input {
        padding: 0.6rem 1rem;
        font-size: 0.95rem;
        border-radius: 8px;
    }
    
    .compact-form .stTextInput > label {
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }
    
    /* Buttons - COMPACT */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--dark-blue) 100%);
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        box-shadow: 0 3px 12px rgba(46, 134, 171, 0.3);
        margin: 0.3rem 0;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 18px rgba(46, 134, 171, 0.4);
    }
    
    /* Forgot password button - special styling */
    .forgot-password-btn {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24) !important;
    }
    
    .forgot-password-btn:hover {
        background: linear-gradient(135deg, #ff5252, #d63031) !important;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        border: 2px solid var(--light-blue);
        border-radius: 10px;
        padding: 0.8rem 1rem;
        font-size: 1rem;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary-blue);
        box-shadow: 0 0 0 3px rgba(46, 134, 171, 0.1);
    }
    
    /* Sidebar welcome message */
    .sidebar-welcome {
        background: rgba(255, 255, 255, 0.15);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: black;
        text-align: center;
    }
    
    /* Auth box */
    .auth-box {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: black;
        text-align: center;
    }
    
    /* Info box */
    .stInfo {
        background: var(--lighter-blue);
        border: 1px solid var(--light-blue);
        border-radius: 12px;
        padding: 1.5rem;
    }
    
    /* Success/Error messages */
    .stSuccess {
        background: #D4F4DD;
        border: 1px solid #4CAF50;
        color: #2E7D32;
        border-radius: 10px;
    }
    
    .stError {
        background: #FFEBEE;
        border: 1px solid #F44336;
        color: #C62828;
        border-radius: 10px;
    }
    
    .stWarning {
        background: #FFF3E0;
        border: 1px solid #FF9800;
        color: #E65100;
        border-radius: 10px;
    }
    
    /* Forgot password specific styling */
    .forgot-password-container {
        background: linear-gradient(135deg, #fff5f5, #ffe8e8);
        border: 2px solid #ff6b6b;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .forgot-password-container h4 {
        color: #d63031;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .verification-code {
        background: #f1f3f4;
        border: 2px solid #34a853;
        border-radius: 8px;
        padding: 1rem;
        font-family: 'Courier New', monospace;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        color: #137333;
        margin: 1rem 0;
        letter-spacing: 0.3rem;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--light-blue), transparent);
        margin: 2rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: var(--primary-blue);
        padding: 2rem;
        background: var(--light-gray);
        border-radius: 15px;
        margin-top: 2rem;
    }
    
    /* Page navigation */
    .nav-item {
        background: rgba(255, 255, 255, 0.1);
        margin: 0.2rem 0;
        border-radius: 8px;
        transition: background 0.3s ease;
    }
    
    .nav-item:hover {
        background: rgba(255, 255, 255, 0.2);
    }
    
    /* Need login message */
    .need-login {
        background: var(--lighter-blue);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        border: 2px solid var(--light-blue);
    }
    
    /* Button group compact styling */
    .button-group-compact {
        display: flex;
        gap: 0.5rem;
        margin-top: 0.8rem;
    }
    
    .button-group-compact .stButton {
        flex: 1;
    }
    
    .button-group-compact .stButton > button {
        margin: 0;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Utility functions for password reset
def generate_verification_code():
    """Tạo mã xác thực 6 chữ số"""
    return ''.join(random.choices(string.digits, k=6))

def send_verification_email(username, code):
    """Giả lập gửi email (trong thực tế sẽ tích hợp email service)"""
    email = get_user_email(username)
    if email:
        print(f"📧 Gửi mã xác thực {code} tới email: {email} cho user: {username}")
        return True
    return False

# Khởi tạo session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

if 'show_auth' not in st.session_state:
    st.session_state.show_auth = False

if 'auth_page' not in st.session_state:  
    st.session_state.auth_page = "Đăng nhập"

# Khởi tạo session state cho chức năng quên mật khẩu
if 'forgot_password_step' not in st.session_state:
    st.session_state.forgot_password_step = 1  # 1: nhập username, 2: nhập mã xác thực, 3: đặt mật khẩu mới

if 'verification_code' not in st.session_state:
    st.session_state.verification_code = None

if 'reset_username' not in st.session_state:
    st.session_state.reset_username = None

if 'code_sent_time' not in st.session_state:
    st.session_state.code_sent_time = None

# Sidebar - luôn hiển thị menu
st.sidebar.title("🫁 Menu Chính")

# Kiểm tra trạng thái đăng nhập và hiển thị thông tin user
if st.session_state.logged_in:
    st.sidebar.markdown(f"""
    <div class="sidebar-welcome">
        <h4>👋 Xin chào!</h4>
        <p><strong>{st.session_state.user['username']}</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.sidebar.button("🚪 Đăng xuất", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.show_auth = False
        st.rerun()
else:
    # Hiển thị form đăng nhập/đăng ký trong sidebar
    st.sidebar.markdown("""
    <div class="auth-box">
        <h4>🔐 Xác thực</h4>
        <p>Đăng nhập để sử dụng đầy đủ tính năng</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.sidebar.button("🚀 Đăng nhập", use_container_width=True):
        st.session_state.show_auth = True
        st.session_state.auth_page = "Đăng nhập"
    
    if st.sidebar.button("📝 Đăng ký", use_container_width=True):
        st.session_state.show_auth = True
        st.session_state.auth_page = "Đăng ký"
    
    if st.sidebar.button("🔑 Quên mật khẩu", use_container_width=True):
        st.session_state.show_auth = True
        st.session_state.auth_page = "Quên mật khẩu"
        st.session_state.forgot_password_step = 1  # Reset về bước đầu

# Hiển thị nội dung trang chủ
# Hiển thị form đăng nhập/đăng ký nếu được yêu cầu
if st.session_state.show_auth and not st.session_state.logged_in:
    # COMPACT HEADER
    st.markdown("""
    <div class="main-header">
        <h1>🫁 Hệ thống Chẩn đoán Bệnh Phổi</h1>
        <p>Công nghệ AI tiên tiến - Chẩn đoán chính xác, nhanh chóng</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Container trung tâm cho form auth - COMPACT
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        # ========== FORM ĐĂNG NHẬP ==========
        if st.session_state.auth_page == "Đăng nhập":
            st.markdown("""
            <div class="login-container">
                <h4>🔐 Đăng nhập</h4>
            </div>
            """, unsafe_allow_html=True)

            # Compact form container
            st.markdown('<div class="compact-form">', unsafe_allow_html=True)
            
            username = st.text_input("👤 Tên đăng nhập", placeholder="Username", key="login_user")
            password = st.text_input("🔒 Mật khẩu", type="password", placeholder="Password", key="login_pass")
            
            st.markdown('</div>', unsafe_allow_html=True)

            # Compact button group
            col_btn1, col_btn2, col_btn3 = st.columns(3)
            
            with col_btn1:
                if st.button("🚀 Đăng nhập", use_container_width=True):
                    if username and password:
                        user = login(username, password)
                        if user:
                            # Kiểm tra trạng thái tài khoản TRƯỚC KHI đăng nhập
                            if user.get("status") == "locked":
                                st.error("🔒 Tài khoản đã bị khóa! Vui lòng liên hệ quản trị viên.")
                            else:
                                # Chỉ cho phép đăng nhập nếu status != "locked"
                                st.session_state.logged_in = True
                                st.session_state.user = user
                                st.session_state.show_auth = False
                                st.success("✅ Đăng nhập thành công!")
                                st.rerun()
                        else:
                            st.error("❌ Sai tên đăng nhập hoặc mật khẩu")
                    else:
                        st.warning("⚠️ Vui lòng nhập đầy đủ thông tin")

            with col_btn2:
                if st.button("📝 Đăng ký", use_container_width=True):
                    st.session_state.auth_page = "Đăng ký"
                    st.rerun()
            
            with col_btn3:
                if st.button("❌ Hủy", use_container_width=True):
                    st.session_state.show_auth = False
                    st.rerun()

            # Link quên mật khẩu
            st.markdown("<hr style='margin: 1rem 0;'>", unsafe_allow_html=True)
            if st.button("🔑 Quên mật khẩu?", use_container_width=True, key="forgot_from_login"):
                st.session_state.auth_page = "Quên mật khẩu"
                st.session_state.forgot_password_step = 1
                st.rerun()

        # ========== FORM ĐĂNG KÝ ==========
        elif st.session_state.auth_page == "Đăng ký":
            st.markdown("""
            <div class="login-container">
                <h4>📝 Tạo tài khoản</h4>
            </div>
            """, unsafe_allow_html=True)

            # Compact form container
            st.markdown('<div class="compact-form">', unsafe_allow_html=True)
            
            username = st.text_input("👤 Tên đăng nhập", placeholder="Username", key="reg_user")
            password = st.text_input("🔒 Mật khẩu", type="password", placeholder="Password", key="reg_pass")
            confirm_password = st.text_input("🔒 Xác nhận mật khẩu", type="password", placeholder="Confirm Password", key="reg_pass2")
            
            st.markdown('</div>', unsafe_allow_html=True)

            # Compact button group
            col_btn1, col_btn2, col_btn3 = st.columns(3)
            
            with col_btn1:
                if st.button("✅ Tạo TK", use_container_width=True):
                    if username and password and confirm_password:
                        if password == confirm_password:
                            try:
                                # Mặc định gán status="active"
                                if register(username, password, status="active"):
                                    st.success("🎉 Đăng ký thành công!")
                                    st.balloons()
                                    st.session_state.auth_page = "Đăng nhập"
                                    st.rerun()
                            except Exception as e:
                                st.error(f"❌ Lỗi: {e}")
                        else:
                            st.error("❌ Mật khẩu không khớp")
                    else:
                        st.warning("⚠️ Nhập đầy đủ thông tin")

            with col_btn2:
                if st.button("🔄 Đăng nhập", use_container_width=True):
                    st.session_state.auth_page = "Đăng nhập"
                    st.rerun()
                    
            with col_btn3:
                if st.button("❌ Hủy", use_container_width=True):
                    st.session_state.show_auth = False
                    st.rerun()

        # ========== FORM QUÊN MẬT KHẨU ==========
        elif st.session_state.auth_page == "Quên mật khẩu":
            # BƯỚC 1: Nhập username
            if st.session_state.forgot_password_step == 1:
                st.markdown("""
                <div class="forgot-password-container">
                    <h4>🔑 Khôi phục mật khẩu</h4>
                    <p style="text-align: center; color: #666;">Bước 1: Nhập tên đăng nhập của bạn</p>
                </div>
                """, unsafe_allow_html=True)

                username = st.text_input("👤 Tên đăng nhập", placeholder="Nhập username cần khôi phục", key="forgot_username")
                
                col_btn1, col_btn2 = st.columns(2)
                
                with col_btn1:
                    # Trong phần xử lý quên mật khẩu - Bước 1, thay thế:
                    if st.button("📧 Gửi mã xác thực", use_container_width=True):
                        if username:
                            # SỬA: Sử dụng hàm check_username_exists từ auth.py
                            if check_username_exists(username):
                                # Tạo mã xác thực
                                verification_code = generate_verification_code()
                                st.session_state.verification_code = verification_code
                                st.session_state.reset_username = username
                                st.session_state.code_sent_time = time.time()
                                
                                # Gửi email
                                if send_verification_email(username, verification_code):
                                    # Chuyển sang bước 2
                                    st.session_state.forgot_password_step = 2
                                    st.success(f"✅ Đã gửi mã xác thực đến email của tài khoản: {username}")
                                    time.sleep(1)
                                    st.rerun()
                                else:
                                    st.error("❌ Không thể gửi email! Vui lòng thử lại.")
                            else:
                                st.error("❌ Tên đăng nhập không tồn tại!")
                        else:
                            st.warning("⚠️ Vui lòng nhập tên đăng nhập")
                
                with col_btn2:
                    if st.button("🔙 Quay lại đăng nhập", use_container_width=True):
                        st.session_state.auth_page = "Đăng nhập"
                        st.rerun()

            # BƯỚC 2: Nhập mã xác thực
            elif st.session_state.forgot_password_step == 2:
                st.markdown("""
                <div class="forgot-password-container">
                    <h4>🔑 Khôi phục mật khẩu</h4>
                    <p style="text-align: center; color: #666;">Bước 2: Nhập mã xác thực</p>
                </div>
                """, unsafe_allow_html=True)

                st.info(f"📧 Mã xác thực đã được gửi đến email của tài khoản: **{st.session_state.reset_username}**")
                
                # Hiển thị mã xác thực để demo (trong thực tế sẽ không hiển thị)
                st.markdown(f"""
                <div class="verification-code">
                    🔐 Mã demo: {st.session_state.verification_code}
                </div>
                <p style="text-align: center; font-size: 0.8rem; color: #666;">
                    (Trong thực tế, mã này sẽ được gửi qua email và không hiển thị ở đây)
                </p>
                """, unsafe_allow_html=True)

                entered_code = st.text_input("🔢 Mã xác thực (6 chữ số)", placeholder="Nhập mã 6 chữ số", key="verification_code_input", max_chars=6)
                
                # Kiểm tra thời gian hết hạn (5 phút)
                if st.session_state.code_sent_time:
                    time_elapsed = time.time() - st.session_state.code_sent_time
                    time_remaining = max(0, 300 - time_elapsed)  # 5 phút = 300 giây
                    
                    if time_remaining > 0:
                        minutes = int(time_remaining // 60)
                        seconds = int(time_remaining % 60)
                        st.info(f"⏰ Mã có hiệu lực trong: {minutes:02d}:{seconds:02d}")
                    else:
                        st.error("❌ Mã xác thực đã hết hạn! Vui lòng yêu cầu mã mới.")

                col_btn1, col_btn2, col_btn3 = st.columns(3)
                
                with col_btn1:
                    if st.button("✅ Xác thực", use_container_width=True):
                        if entered_code:
                            if len(entered_code) == 6 and entered_code == st.session_state.verification_code:
                                if time_remaining > 0:
                                    st.session_state.forgot_password_step = 3
                                    st.success("✅ Xác thực thành công!")
                                    time.sleep(1)
                                    st.rerun()
                                else:
                                    st.error("❌ Mã xác thực đã hết hạn!")
                            else:
                                st.error("❌ Mã xác thực không đúng!")
                        else:
                            st.warning("⚠️ Vui lòng nhập mã xác thực")
                
                with col_btn2:
                    if st.button("🔄 Gửi lại mã", use_container_width=True):
                        # Tạo mã mới
                        new_code = generate_verification_code()
                        st.session_state.verification_code = new_code
                        st.session_state.code_sent_time = time.time()
                        send_verification_email(st.session_state.reset_username, new_code)
                        st.success("✅ Đã gửi lại mã xác thực!")
                        time.sleep(1)
                        st.rerun()
                
                with col_btn3:
                    if st.button("❌ Hủy", use_container_width=True):
                        st.session_state.auth_page = "Đăng nhập"
                        st.session_state.forgot_password_step = 1
                        st.rerun()

            # BƯỚC 3: Đặt mật khẩu mới
            elif st.session_state.forgot_password_step == 3:
                st.markdown("""
                <div class="forgot-password-container">
                    <h4>🔑 Khôi phục mật khẩu</h4>
                    <p style="text-align: center; color: #666;">Bước 3: Đặt mật khẩu mới</p>
                </div>
                """, unsafe_allow_html=True)

                st.success(f"✅ Xác thực thành công cho tài khoản: **{st.session_state.reset_username}**")
                
                new_password = st.text_input("🔒 Mật khẩu mới", type="password", placeholder="Nhập mật khẩu mới", key="new_password")
                confirm_new_password = st.text_input("🔒 Xác nhận mật khẩu mới", type="password", placeholder="Nhập lại mật khẩu mới", key="confirm_new_password")
                
                # Hiển thị yêu cầu mật khẩu
                st.info("""
                **📋 Yêu cầu mật khẩu:**
                - Ít nhất 6 ký tự
                - Nên có chữ hoa, chữ thường và số
                - Không chứa khoảng trắng
                """)
                
                col_btn1, col_btn2 = st.columns(2)
                
                with col_btn1:
                    if st.button("💾 Cập nhật mật khẩu", use_container_width=True):
                        if new_password and confirm_new_password:
                            if new_password == confirm_new_password:
                                if len(new_password) >= 6:
                                    # Cập nhật mật khẩu trong database
                                    if reset_password_in_db(st.session_state.reset_username, new_password):
                                        st.success("🎉 Đặt lại mật khẩu thành công!")
                                        st.balloons()
                                        
                                        # Reset tất cả state và quay về đăng nhập
                                        st.session_state.auth_page = "Đăng nhập"
                                        st.session_state.forgot_password_step = 1
                                        st.session_state.verification_code = None
                                        st.session_state.reset_username = None
                                        st.session_state.code_sent_time = None
                                        
                                        time.sleep(2)
                                        st.rerun()
                                    else:
                                        st.error("❌ Có lỗi xảy ra khi cập nhật mật khẩu!")
                                else:
                                    st.error("❌ Mật khẩu phải có ít nhất 6 ký tự!")
                            else:
                                st.error("❌ Mật khẩu xác nhận không khớp!")
                        else:
                            st.warning("⚠️ Vui lòng nhập đầy đủ thông tin")
                
                with col_btn2:
                    if st.button("🔙 Quay lại đăng nhập", use_container_width=True):
                        st.session_state.auth_page = "Đăng nhập"
                        st.session_state.forgot_password_step = 1
                        st.rerun()

else:
    # Trang chủ chính - luôn hiển thị cho tất cả người dùng
    st.markdown("""
    <div class="main-header">
        <h1>🫁 Hệ thống Chẩn đoán Bệnh Phổi AI</h1>
        <p>Chào mừng bạn đến với hệ thống chẩn đoán thông minh</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Thống kê nhanh
    st.markdown("### 📈 Thống kê tổng quan")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stats-card">
            <h3>1,250+</h3>
            <p>Ca chẩn đoán thành công</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stats-card">
            <h3>95.8%</h3>
            <p>Độ chính xác trung bình</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stats-card">
            <h3>2.3s</h3>
            <p>Thời gian xử lý trung bình</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stats-card">
            <h3>24/7</h3>
            <p>Hỗ trợ liên tục</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Chức năng chính
    st.markdown("### 🎯 Chức năng chính của hệ thống")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🔍 Chẩn đoán từ X-quang</h4>
            <p>• Tải lên ảnh X-quang ngực chất lượng cao</p>
            <p>• Phân tích tự động bằng AI tiên tiến</p>
            <p>• Nhận kết quả chi tiết với tỷ lệ tin cậy</p>
            <p>• Xuất báo cáo PDF chuyên nghiệp</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Lịch sử & Thống kê</h4>
            <p>• Xem lại các ca đã chẩn đoán trước đó</p>
            <p>• So sánh kết quả theo thời gian</p>
            <p>• Phân tích xu hướng bệnh lý</p>
            <p>• Báo cáo thống kê tổng hợp</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🎓 Trung tâm kiến thức</h4>
            <p>• Thư viện bệnh phổi thường gặp</p>
            <p>• Hướng dẫn đọc X-quang cơ bản</p>
            <p>• Cập nhật nghiên cứu y khoa mới nhất</p>
            <p>• Video hướng dẫn chi tiết</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>🤖 AI Tư vấn thông minh</h4>
            <p>• Tư vấn sơ bộ dựa trên triệu chứng</p>
            <p>• Gợi ý các xét nghiệm cần thiết</p>
            <p>• Hỗ trợ 24/7 với chatbot AI</p>
            <p>• Kết nối với bác sĩ chuyên khoa</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Hướng dẫn sử dụng
    st.markdown("### 🚀 Hướng dẫn sử dụng nhanh")
    
    st.info("""
    **📋 Các bước thực hiện:**
    
    1. **🔍 Chẩn đoán:** Chọn "Chẩn đoán" trong menu → Đăng nhập nếu chưa → Tải ảnh X-quang → Nhận kết quả
    2. **📊 Theo dõi:** Vào "Lịch sử" để xem các ca đã chẩn đoán và thống kê chi tiết  
    3. **🤖 Tư vấn:** Sử dụng "AI Tư vấn" để được hỗ trợ và tư vấn sơ bộ
    4. **📚 Học hỏi:** Tham khảo "Trung tâm kiến thức" để nâng cao kiến thức y khoa
    
    💡 **Lưu ý quan trọng:** 
    • Sử dụng ảnh X-quang rõ nét, chất lượng cao để có kết quả chính xác nhất
    • Kết quả chỉ mang tính tham khảo, cần có ý kiến của bác sĩ chuyên khoa
    • Dữ liệu của bạn được bảo mật tuyệt đối theo tiêu chuẩn y tế
    
    🔑 **Chức năng mới:** 
    • **Quên mật khẩu:** Khôi phục tài khoản dễ dàng qua 3 bước đơn giản
    • **Bảo mật cao:** Mã xác thực 6 chữ số với thời gian hiệu lực 5 phút
    • **Tự động hóa:** Gửi mã qua email và cập nhật mật khẩu tức thời
    """)

# Footer - luôn hiển thị
st.markdown("""
<hr>
<div class="footer">
    <h4>🫁 Hệ thống Chẩn đoán Bệnh Phổi </h4>
    <p><strong>Công nghệ tiên tiến - Chẩn đoán chính xác</strong></p>
    <p>🏥 Phát triển bởi Đội ngũ Y tế Công nghệ | 📞 Hỗ trợ: 0321564789</p>
    <p>🌐 Website: <strong>http://localhost:8501/</strong> | ✉️ Email: pneumonia@gmail.com</p>
</div>
""", unsafe_allow_html=True)