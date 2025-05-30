# dashboard.py
import json
from datetime import datetime
from news_service import NewsService
from weather_service import WeatherService
from country_service import CountryService

def obtener_icono_climatico(descripcion):
    desc = descripcion.lower()
    if "lluvia" in desc:
        return "🌧️"
    elif "nieve" in desc:
        return "❄️"
    elif "tormenta" in desc:
        return "⛈️"
    elif "nublado" in desc:
        return "☁️"
    elif "soleado" in desc or "despejado" in desc:
        return "☀️"
    elif "niebla" in desc:
        return "🌫️"
    else:
        return "🌤️"

def correlacionar_noticias_con_clima(noticias, clima_descripcion):
    clima_keywords = clima_descripcion.lower().split()
    noticias_relacionadas = []

    for noticia in noticias:
        titulo = noticia.get("title", "").lower()
        descripcion = noticia.get("description", "").lower() if noticia.get("description") else ""
        if any(palabra in titulo or palabra in descripcion for palabra in clima_keywords):
            noticias_relacionadas.append(noticia)
    
    return noticias_relacionadas

def main(country_code, ciudad):
    country_code = country_code.strip().lower()
    ciudad = ciudad.strip()

    # Inicializar servicios
    news_service = NewsService()
    weather_service = WeatherService()

    # Obtener clima
    weather = weather_service.get_weather(ciudad)
    if not weather:
        print("No se pudo obtener información del clima.")
        return

    icono_clima = obtener_icono_climatico(weather.get("descripcion", ""))

    # Obtener noticias
    noticias_data = news_service.get_top_headlines(country=country_code, page_size=10)
    if noticias_data and noticias_data.get("totalResults", 0) > 0:
        noticias = noticias_data.get("articles", [])
    else:
        nombre_pais = "Chile"  # fallback
        noticias_data = news_service.search_news(query=nombre_pais, page_size=10)
        noticias = noticias_data.get("articles", []) if noticias_data else []

    # Correlación con clima
    relacionadas = correlacionar_noticias_con_clima(noticias, weather.get("descripcion", ""))

    # Mostrar en consola
    print("\n===== DASHBOARD DEL DÍA =====")
    print(f"🌍 País: {country_code.upper()} | Ciudad: {ciudad}")
    print(f"{icono_clima} Clima: {weather.get('descripcion', '').capitalize()} | Temp: {weather.get('temperatura', '')}°C\n")

    print("📰 Principales noticias:")
    for i, article in enumerate(noticias[:5], 1):
        print(f"{i}. {article.get('title', 'Sin título')}")
        print(f"   Fuente: {article.get('source', {}).get('name', 'Desconocida')}")
        print(f"   URL: {article.get('url', '')}\n")

    if relacionadas:
        print("🔗 Noticias relacionadas con el clima:")
        for r in relacionadas:
            print(f"- {r.get('title')}")

    # Crear objeto de reporte
    reporte = {
        "fecha": datetime.now().isoformat(),
        "pais": country_code.upper(),
        "ciudad": ciudad,
        "clima": weather,
        "noticias": noticias[:5],
        "noticias_relacionadas_con_clima": relacionadas
    }

    # Guardar como JSON
    with open("reporte_diario.json", "w", encoding="utf-8") as f:
        json.dump(reporte, f, ensure_ascii=False, indent=4)

    # Exportar a TXT
    with open("reporte_diario.txt", "w", encoding="utf-8") as f:
        f.write(f"Reporte Diario - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"País: {country_code.upper()} | Ciudad: {ciudad}\n")
        f.write(f"Clima: {weather.get('descripcion', '').capitalize()} | Temp: {weather.get('temperatura', '')}°C\n\n")
        f.write("Principales noticias:\n")
        for i, article in enumerate(noticias[:5], 1):
            f.write(f"{i}. {article.get('title', 'Sin título')} ({article.get('source', {}).get('name', 'Desconocida')})\n")
            f.write(f"   URL: {article.get('url', '')}\n\n")
        if relacionadas:
            f.write("Noticias relacionadas con el clima:\n")
            for r in relacionadas:
                f.write(f"- {r.get('title')}\n")

    print("✅ Reportes guardados en 'reporte_diario.json' y 'reporte_diario.txt'")

# No se ejecuta solo, se llama desde main.py
