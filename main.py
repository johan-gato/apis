import time
from datetime import datetime, timedelta
import re
import os
from dashboard import main as generar_dashboard
from gmail_service import enviar_correo

def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def pedir_programacion_envio():
    print("\n📤 ¿Cuándo deseas enviar el correo?")
    print("1. Ahora mismo")
    print("2. En X minutos")
    print("3. En una fecha y hora específica (DD-MM-YYYY HH:MM)")

    opcion = input("Selecciona opción (1/2/3): ").strip()

    if opcion == "1":
        return datetime.now()
    elif opcion == "2":
        try:
            minutos = int(input("¿Cuántos minutos? ").strip())
            return datetime.now() + timedelta(minutes=minutos)
        except ValueError:
            print("❌ Valor inválido. Enviando ahora.")
            return datetime.now()
    elif opcion == "3":
        try:
            fecha_hora = input("Fecha y hora (ej: 31-05-2025 08:00): ").strip()
            return datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M")
        except ValueError:
            print("❌ Formato inválido. Enviando ahora.")
            return datetime.now()
    else:
        print("❌ Opción inválida. Enviando ahora.")
        return datetime.now()

if __name__ == "__main__":
    pais = input("🌎 Ingresa el código del país (ej: cl, us, ar): ").strip()
    ciudad = input("🏙️ Ingresa la ciudad a consultar (ej: Santiago, New York, Buenos Aires): ").strip()

    print("🔧 Generando reporte desde dashboard.py ...")
    try:
        generar_dashboard(pais, ciudad)
        if not os.path.exists("reporte_diario.txt"):
            print("❌ reporte_diario.txt no encontrado. Verifica dashboard.py.")
            exit(1)

        with open("reporte_diario.txt", "r", encoding="utf-8") as f:
            reporte = f.read()

        print("✅ Reporte generado.\n")
    except Exception as e:
        print(f"❌ Error generando reporte: {e}")
        exit(1)

    destinatario = input("✉️ Correo destinatario: ").strip()
    if not destinatario or not validar_correo(destinatario):
        print("❌ Correo inválido.")
        exit(1)

    momento_envio = pedir_programacion_envio()
    espera = (momento_envio - datetime.now()).total_seconds()

    if espera > 0:
        print(f"⏳ Esperando {round(espera/60,2)} minutos para enviar correo...")
        time.sleep(espera)

    print("📨 Enviando correo...")
    try:
        enviar_correo(reporte, destinatario)
        print("✅ Correo enviado exitosamente.")
    except Exception as e:
        if "535" in str(e):
            print("❌ Error autenticación SMTP: revisa usuario y contraseña.")
        else:
            print(f"❌ Error enviando correo: {e}")
