import time
from datetime import datetime, timedelta
from gmail_service import enviar_correo
from country_service import obtener_info_pais
from weather_service import obtener_clima
from news_service import NewsService
import os

def generar_reporte():
    country_data = obtener_info_pais('CL')  # Chile
    weather = obtener_clima('Santiago')

    news_service = NewsService()
    noticias_data = news_service.get_top_headlines(country="cl", page_size=5)

    if not noticias_data or noticias_data.get("totalResults", 0) == 0:
        print("No hay resultados en top-headlines. Buscando con search_news...")
        noticias_data = news_service.search_news(query="Chile", page_size=5)

    noticias = noticias_data.get("articles", [])[:5] if noticias_data else []

    noticias_texto = "\n".join(
        [f"- {noticia['title']} ({noticia.get('source', {}).get('name', 'Desconocido')})" for noticia in noticias]
    ) if noticias else "No se encontraron noticias."

    reporte = f"""🧾 REPORTE AUTOMÁTICO:

🌎 Datos del país:
{country_data}

🌤️ Clima actual:
{weather}

📰 Noticias destacadas:
{noticias_texto}
"""
    return reporte

def pedir_programacion_envio():
    print("\n📤 ¿Cuándo deseas enviar el correo?")
    print("1. Ahora mismo")
    print("2. En X minutos")
    print("3. En una fecha y hora específica (formato: DD-MM-YYYY HH:MM)")

    opcion = input("Selecciona una opción (1/2/3): ").strip()

    if opcion == "1":
        return datetime.now()
    elif opcion == "2":
        try:
            minutos = int(input("¿Cuántos minutos quieres esperar? ").strip())
            return datetime.now() + timedelta(minutes=minutos)
        except ValueError:
            print("❌ Valor inválido. Se enviará ahora.")
            return datetime.now()
    elif opcion == "3":
        try:
            fecha_hora = input("Ingresa la fecha y hora (ejemplo: 31-05-2025 08:00): ").strip()
            return datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M")
        except ValueError:
            print("❌ Formato incorrecto. Se enviará ahora.")
            return datetime.now()
    else:
        print("❌ Opción inválida. Se enviará ahora.")
        return datetime.now()

if __name__ == "__main__":
    print("🔧 Generando reporte completo...")
    try:
        reporte = generar_reporte()

        with open("reporte_final.txt", "w", encoding='utf-8') as archivo:
            archivo.write(reporte)

        print("✅ Reporte generado. Guardado en reporte_final.txt.\n")
    except Exception as e:
        print(f"❌ Error generando el reporte: {e}")
        exit(1)

    destinatario = input("✉️ Ingresa el correo del destinatario: ").strip()
    if not destinatario:
        print("❌ Debes ingresar un correo válido.")
        exit(1)

    momento_envio = pedir_programacion_envio()
    espera = (momento_envio - datetime.now()).total_seconds()

    if espera > 0:
        print(f"\n⏳ Esperando {round(espera/60, 2)} minutos para enviar el correo...")
        time.sleep(espera)

    print("📨 Enviando correo...")
    try:
        enviar_correo(reporte, destinatario)
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")
