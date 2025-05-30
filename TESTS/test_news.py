from news_service import NewsService

def main():
    news_service = NewsService()
    country_code = input("Ingrese código de país para las noticias (ej: cl, us, ar): ").strip().lower()

    # Intentar obtener noticias top-headlines
    result = news_service.get_top_headlines(country=country_code, page_size=5)

    if not result or result.get("totalResults", 0) == 0:
        print(f"No hay resultados en top-headlines para '{country_code}'. Buscando con search_news...")
        # Buscar con término genérico: nombre del país (puedes mapear códigos a nombres si quieres)
        search_result = news_service.search_news(query=country_code, page_size=5)
        if search_result and search_result.get("totalResults", 0) > 0:
            articles = search_result.get("articles", [])
        else:
            print("No se encontraron noticias con search_news.")
            return
    else:
        articles = result.get("articles", [])

    print(f"Noticias principales para país: {country_code.upper()}")
    for i, article in enumerate(articles, 1):
        title = article.get("title", "Sin título")
        source = article.get("source", {}).get("name", "Fuente desconocida")
        url = article.get("url", "")
        print(f"{i}. {title}\n   Fuente: {source}\n   URL: {url}\n")

if __name__ == "__main__":
    main()
