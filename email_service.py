import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
import os

# Email configuration from environment
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
EMAIL_FROM = os.getenv("EMAIL_FROM", SMTP_USER)

def send_email(
    to_email: str,
    subject: str,
    html_content: str,
    text_content: Optional[str] = None
) -> bool:
    """Send email using SMTP"""
    if not SMTP_USER or not SMTP_PASSWORD:
        print(f"[EMAIL] SMTP not configured. Would send to {to_email}: {subject}")
        return False
    
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = EMAIL_FROM
        msg["To"] = to_email
        
        if text_content:
            part1 = MIMEText(text_content, "plain")
            msg.attach(part1)
        
        part2 = MIMEText(html_content, "html")
        msg.attach(part2)
        
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        
        print(f"[EMAIL] Sent successfully to {to_email}: {subject}")
        return True
    except Exception as e:
        print(f"[EMAIL] Error sending email to {to_email}: {str(e)}")
        return False

def send_order_confirmation_email(customer_email: str, customer_name: str, order_id: int):
    """Send order confirmation email"""
    subject = f"Order #{order_id} - Konfirmasi Pickup Minyak Jelantah"
    html_content = f"""
    <html>
    <body>
        <h2>Terima Kasih, {customer_name}!</h2>
        <p>Order pickup minyak jelantah Anda telah berhasil dibuat.</p>
        <p><strong>Order ID:</strong> #{order_id}</p>
        <p>Kurir kami akan segera menghubungi Anda untuk jadwal pickup.</p>
        <p>Terima kasih telah menggunakan layanan JelantahGO!</p>
    </body>
    </html>
    """
    return send_email(customer_email, subject, html_content)

def send_order_assigned_email(customer_email: str, customer_name: str, order_id: int, courier_name: str):
    """Send email when courier is assigned"""
    subject = f"Order #{order_id} - Kurir Telah Ditugaskan"
    html_content = f"""
    <html>
    <body>
        <h2>Halo {customer_name}!</h2>
        <p>Kurir telah ditugaskan untuk order pickup Anda.</p>
        <p><strong>Order ID:</strong> #{order_id}</p>
        <p><strong>Kurir:</strong> {courier_name}</p>
        <p>Kurir akan segera menghubungi Anda untuk koordinasi pickup.</p>
    </body>
    </html>
    """
    return send_email(customer_email, subject, html_content)

def send_order_completed_email(customer_email: str, customer_name: str, order_id: int, total_amount: float):
    """Send email when order is completed"""
    subject = f"Order #{order_id} - Pickup Selesai"
    html_content = f"""
    <html>
    <body>
        <h2>Terima Kasih, {customer_name}!</h2>
        <p>Order pickup minyak jelantah Anda telah selesai.</p>
        <p><strong>Order ID:</strong> #{order_id}</p>
        <p><strong>Total Pembayaran:</strong> Rp {total_amount:,.0f}</p>
        <p>Bukti pembayaran akan dikirimkan oleh admin melalui aplikasi.</p>
        <p>Terima kasih telah menggunakan layanan JelantahGO!</p>
    </body>
    </html>
    """
    return send_email(customer_email, subject, html_content)

def send_payment_proof_email(customer_email: str, customer_name: str, order_id: int, file_url: str):
    """Send email when payment proof is uploaded"""
    subject = f"Order #{order_id} - Bukti Pembayaran Tersedia"
    html_content = f"""
    <html>
    <body>
        <h2>Halo {customer_name}!</h2>
        <p>Bukti pembayaran untuk order Anda telah tersedia.</p>
        <p><strong>Order ID:</strong> #{order_id}</p>
        <p>Silakan cek bukti pembayaran di aplikasi atau klik link berikut:</p>
        <p><a href="{file_url}">Lihat Bukti Pembayaran</a></p>
    </body>
    </html>
    """
    return send_email(customer_email, subject, html_content)

