import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Cấu hình email - thay đổi theo gmail/outlook của bạn
EMAIL_HOST = "smtp.gmail.com"  # Gmail SMTP
EMAIL_PORT = 587
EMAIL_USER = os.getenv("EMAIL_USER", "your_email@gmail.com")  # Email của bạn
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "your_app_password")  # App password
EMAIL_FROM_NAME = "Hệ thống Chẩn đoán Bệnh Phổi"

def send_verification_email_real(to_email, username, verification_code):
    """Gửi email xác thực thực sự"""
    try:
        # Tạo nội dung email
        subject = "🔐 Mã xác thực khôi phục mật khẩu"
        
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="background: linear-gradient(135deg, #2E86AB 0%, #1B5E7F 100%); color: white; padding: 20px; border-radius: 10px 10px 0 0;">
                    <h2>🫁 Hệ thống Chẩn đoán Bệnh Phổi</h2>
                </div>
                
                <div style="background: #f8f9fa; padding: 30px; border-radius: 0 0 10px 10px; border: 1px solid #e9ecef;">
                    <h3 style="color: #2E86AB;">Khôi phục mật khẩu</h3>
                    <p>Xin chào <strong>{username}</strong>,</p>
                    
                    <p>Bạn đã yêu cầu khôi phục mật khẩu cho tài khoản của mình.</p>
                    
                    <div style="background: #fff; border: 2px solid #2E86AB; border-radius: 8px; padding: 20px; text-align: center; margin: 20px 0;">
                        <p style="margin: 0; color: #666;">Mã xác thực của bạn:</p>
                        <h1 style="font-size: 36px; color: #2E86AB; letter-spacing: 5px; margin: 10px 0; font-family: monospace;">
                            {verification_code}
                        </h1>
                        <p style="margin: 0; color: #666; font-size: 14px;">Mã có hiệu lực trong 5 phút</p>
                    </div>
                    
                    <p><strong>⚠️ Lưu ý quan trọng:</strong></p>
                    <ul style="color: #666;">
                        <li>Mã xác thực chỉ có hiệu lực trong 5 phút</li>
                        <li>Không chia sẻ mã này với bất kỳ ai</li>
                        <li>Nếu bạn không yêu cầu khôi phục mật khẩu, hãy bỏ qua email này</li>
                    </ul>
                    
                    <hr style="border: 1px solid #e9ecef; margin: 20px 0;">
                    
                    <p style="color: #666; font-size: 12px; text-align: center;">
                        Email được gửi tự động vào {datetime.now().strftime("%d/%m/%Y %H:%M")}<br>
                        🏥 Hệ thống Chẩn đoán Bệnh Phổi AI<br>
                        📞 Hỗ trợ: 0321564789 | ✉️ pneumonia@gmail.com
                    </p>
                </div>
            </body>
        </html>
        """
        
        # Tạo email
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = f"{EMAIL_FROM_NAME} <{EMAIL_USER}>"
        msg['To'] = to_email
        
        # Thêm nội dung HTML
        html_part = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(html_part)
        
        # Gửi email
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Đã gửi email thành công đến: {to_email}")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi gửi email: {e}")
        return False

def send_password_changed_notification(to_email, username):
    """Gửi thông báo mật khẩu đã được thay đổi"""
    try:
        subject = "🔐 Mật khẩu đã được thay đổi"
        
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%); color: white; padding: 20px; border-radius: 10px 10px 0 0;">
                    <h2>🫁 Hệ thống Chẩn đoán Bệnh Phổi</h2>
                </div>
                
                <div style="background: #f8f9fa; padding: 30px; border-radius: 0 0 10px 10px; border: 1px solid #e9ecef;">
                    <h3 style="color: #28a745;">Mật khẩu đã được cập nhật</h3>
                    <p>Xin chào <strong>{username}</strong>,</p>
                    
                    <div style="background: #d4edda; border: 1px solid #c3e6cb; border-radius: 8px; padding: 15px; margin: 20px 0;">
                        <p style="margin: 0; color: #155724;">
                            ✅ Mật khẩu cho tài khoản của bạn đã được thay đổi thành công vào {datetime.now().strftime("%d/%m/%Y lúc %H:%M")}.
                        </p>
                    </div>
                    
                    <p><strong>🛡️ Bảo mật tài khoản:</strong></p>
                    <ul style="color: #666;">
                        <li>Nếu bạn KHÔNG thực hiện thay đổi này, hãy liên hệ ngay với chúng tôi</li>
                        <li>Đăng nhập và kiểm tra hoạt động tài khoản</li>
                        <li>Sử dụng mật khẩu mạnh và không chia sẻ với ai</li>
                    </ul>
                    
                    <div style="text-align: center; margin: 30px 0;">
                        <a href="http://localhost:8501" style="background: #28a745; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold;">
                            🚀 Đăng nhập ngay
                        </a>
                    </div>
                    
                    <hr style="border: 1px solid #e9ecef; margin: 20px 0;">
                    
                    <p style="color: #666; font-size: 12px; text-align: center;">
                        🏥 Hệ thống Chẩn đoán Bệnh Phổi AI<br>
                        📞 Hỗ trợ: 0321564789 | ✉️ pneumonia@gmail.com
                    </p>
                </div>
            </body>
        </html>
        """
        
        # Tạo và gửi email
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = f"{EMAIL_FROM_NAME} <{EMAIL_USER}>"
        msg['To'] = to_email
        
        html_part = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(html_part)
        
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Đã gửi thông báo mật khẩu thay đổi đến: {to_email}")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi gửi thông báo: {e}")
        return False