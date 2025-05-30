# gmail_service.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def enviar_correo(reporte, destinatario):
    remitente = "tucorreo@gmail.com"
    contraseña = "tu_contraseña_app"  # Usa contraseña de aplicación, no la tuya real

    # Crear mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Reporte generado automáticamente'
    mensaje.attach(MIMEText(reporte, 'plain'))

    # Esperar 5 minutos (300 segundos)
    print("Esperando 5 minutos antes de enviar el correo...")
    time.sleep(300)

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        servidor.send_message(mensaje)
        servidor.quit()
        print("Correo enviado con éxito.")
    except Exception as e:
        print("Error al enviar el correo:", e)