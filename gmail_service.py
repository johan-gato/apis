# gmail_service.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_REMITENTE = os.getenv("EMAIL_REMITENTE")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def enviar_correo(contenido, destinatario):
    if not EMAIL_REMITENTE or not EMAIL_PASSWORD:
        raise ValueError("❌ EMAIL_REMITENTE o EMAIL_PASSWORD no están definidos. Verifica tu archivo .env.")

    if not contenido or not destinatario:
        raise ValueError("❌ El contenido o el destinatario están vacíos.")

    asunto = "📬 Reporte Automático - Clima y Noticias"

    mensaje = MIMEMultipart()
    mensaje["From"] = EMAIL_REMITENTE
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto

    cuerpo = MIMEText(contenido, "plain", "utf-8")
    mensaje.attach(cuerpo)

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(EMAIL_REMITENTE, EMAIL_PASSWORD)
        servidor.sendmail(EMAIL_REMITENTE, destinatario, mensaje.as_string())
        servidor.quit()
        print(f"✅ Correo enviado exitosamente a {destinatario}")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")
        raise
