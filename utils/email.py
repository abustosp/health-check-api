import smtplib
import ssl
import os
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# import dotenv

# dotenv.load_dotenv()

def send_email(to_email: str, subject: str, body: str):
    message = MIMEMultipart()
    message["From"] = os.getenv("SMTP_FROM_EMAIL")
    message["To"] = to_email
    message["Subject"] = subject
    
    message.attach(MIMEText(body, "html"))

    context = ssl._create_unverified_context()

    try:
        with smtplib.SMTP(host=os.getenv("SMTP_SERVER"), port=os.getenv("SMTP_PORT")) as server:
            server.starttls(context=context)
            server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
            server.send_message(message)

        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

def generate_mail_body(servicios: list) -> str:
    # Cargar template
    with open(os.getenv("TEMPLATE_PATH"), "r", encoding="utf-8") as f:
        email_template = f.read()

    # Normalizar y armar ítems <li>
    items = []
    for servicio in servicios:
        items.append(f"<li><span class=\"highlight\">{servicio}</span></li>")

    servicios_html = "\n        ".join(items) if items else "<li>(sin elementos)</li>"

    # Inyectar en el placeholder
    return email_template.replace("{{SERVICIOS}}", servicios_html)
