# main.py

from gmail_service import enviar_correo
from country_service import obtener_info_pais
from weather_service import obtener_clima
from .news_service import NewsService

def generar_reporte():
    country_data = obtener_info_pais('CL')  # Chile
    weather = obtener_clima('Santiago')
    noticias = NewsService('Chile')

    reporte = f"""🧾 REPORTE AUTOMÁTICO:
    
🌎 Datos del país:
{country_data}

🌤️ Clima actual:
{weather}

📰 Noticias destacadas:
{noticias}
"""
    return reporte

if __name__ == "__main__":
    print("Generando reporte completo...")
    reporte = generar_reporte()

    with open("reporte_final.txt", "w", encoding='utf-8') as archivo:
        archivo.write(reporte)

    print("Reporte generado. Guardado en reporte_final.txt.")

    destinatario = "destinatario@correo.com"
    enviar_correo(reporte, destinatario)