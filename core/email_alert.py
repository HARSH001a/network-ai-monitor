import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "network.alert001@gmail.com"
APP_PASSWORD = "zsoaflulelvesvji"
RECEIVER_EMAIL = "sojitraharsh001@gmail.com"

LOG_FILE = "email_error.log"

def send_email_alert(subject, message):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=15)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

    except Exception:
        with open(LOG_FILE, "a") as f:
            f.write("\n" + traceback.format_exc())
