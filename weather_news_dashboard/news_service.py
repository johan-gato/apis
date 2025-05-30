import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NewsService:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2"
        if not self.api_key:
            raise ValueError("NEWS_API_KEY no está configurada en .env")

    def get_top_headlines(self, country="us", category=None, page=1, page_size=20):
        url = f"{self.base_url}/top-headlines"
        params = {
            "apiKey": self.api_key,
            "country": country,
            "page": page,
            "pageSize": page_size
        }
        if category:
            params["category"] = category
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get("totalResults", 0) > 0:
                return data
            else:
                print(f"No hay resultados en top-headlines para '{country}'. Buscando con search_news...")
                country_name = self.get_country_name(country)
                return self.search_news(query=country_name, page=page, page_size=page_size)
        else:
            print(f"Error al consultar NewsAPI (status: {response.status_code}):")
            print(response.json())
            return None

    def search_news(self, query, from_date=None, to_date=None, language="es", page=1, page_size=20):
        url = f"{self.base_url}/everything"
        params = {
            "apiKey": self.api_key,
            "q": query,
            "language": language,
            "page": page,
            "pageSize": page_size
        }
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

    def get_country_name(self, country_code):
        countries = {
            "us": "United States",
            "cl": "Chile",
            "ar": "Argentina",
            "mx": "Mexico",
            "co": "Colombia",
            "br": "Brazil",
        }
        return countries.get(country_code.lower(), country_code)

    def filter_news_by_condition(self, articles, condition_keywords):
        filtered = []
        for article in articles:
            title = article.get("title", "").lower()
            description = article.get("description", "").lower() if article.get("description") else ""
            content = article.get("content", "").lower() if article.get("content") else ""

            text = " ".join([title, description, content])
            if any(keyword.lower() in text for keyword in condition_keywords):
                filtered.append(article)
        return filtered
