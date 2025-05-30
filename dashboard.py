# dashboard.py
import json
from datetime import datetime
from news_service import NewsService
from weather_service import WeatherService
from country_service import CountryService

def main():
    country_code = input("Ingrese el código del país (ej: cl, us, ar): ").strip().lower()
    
    # Inicializar servicios
    news_service = NewsService()
    weather_service = WeatherService()
    country_service = CountryService()

    # Obtener nombre de capital
    capital = country_service.get_capital_by_country_code(country_code)
    if not capital:
        print(f"No se encontró la capital para el país '{country_code}'")
        return

    # Obtener clima
    weather = weather_service.get_weather(capital)
    if not weather:
        print("No se pudo obtener información del clima.")
        return

    # Obtener noticias
    noticias_data = news_service.get_top_headlines(country=country_code, page_size=5)
    if noticias_data and noticias_data.get("totalResults", 0) > 0:
        noticias = noticias_data.get("articles", [])
    else:
        nombre_pais = news_service.get_country_name(country_code)
        noticias_data = news_service.search_news(query=nombre_pais, page_size=5)
        noticias = noticias_data.get("articles", []) if noticias_data else []

    # Mostrar por consola
    print("\n===== DASHBOARD DEL DÍA =====")
    print(f"🌍 País: {country_code.upper()} | Capital: {capital}")
    print(f"🌤️  Clima: {weather.get('description', '')} | Temp: {weather.get('temperature', '')}°C\n")

    print("📰 Principales noticias:")
    for i, article in enumerate(noticias, 1):
        print(f"{i}. {article.get('title', 'Sin título')}")
        print(f"   Fuente: {article.get('source', {}).get('name', 'Desconocida')}")
        print(f"   URL: {article.get('url', '')}\n")

    # Guardar en JSON
    reporte = {
        "fecha": datetime.now().isoformat(),
        "pais": country_code.upper(),
        "capital": capital,
        "clima": weather,
        "noticias": noticias[:5]  # limitar a 5 noticias
    }

    with open("reporte_diario.json", "w", encoding="utf-8") as f:
        json.dump(reporte, f, ensure_ascii=False, indent=4)

    print("✅ Reporte guardado en 'reporte_diario.json'")

if __name__ == "__main__":
    main()
