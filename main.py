from gmail_service import enviar_correo
from country_service import obtener_info_pais
from weather_service import obtener_clima
from news_service import NewsService

def generar_reporte():
    country_data = obtener_info_pais('CL')  # Chile
    weather = obtener_clima('Santiago')

    news_service = NewsService()
    noticias_data = news_service.get_top_headlines(country="cl")
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

if __name__ == "__main__":
    print("Generando reporte completo...")
    reporte = generar_reporte()

    with open("reporte_final.txt", "w", encoding='utf-8') as archivo:
        archivo.write(reporte)

    print("Reporte generado. Guardado en reporte_final.txt.")

    destinatario = "destinatario@correo.com"
    enviar_correo(reporte, destinatario)