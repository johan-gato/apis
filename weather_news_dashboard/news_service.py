import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

class NewsService:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2"
        if not self.api_key:
            raise ValueError("NEWS_API_KEY no está configurada en .env")

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        logging.error(f"Error {response.status_code}: {response.text}")
        return None

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
        data = self._handle_response(response)

        if data and data.get("totalResults", 0) > 0:
            return data
        else:
            logging.info(f"No hay resultados en top-headlines para '{country}'. Buscando con search_news...")
            country_name = self.get_country_name(country)
            return self.search_news(query=country_name, page=page, page_size=page_size)

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
        return self._handle_response(response)

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
            text = " ".join(filter(None, [
                article.get("title", ""),
                article.get("description", ""),
                article.get("content", "")
            ])).lower()
            if any(keyword.lower() in text for keyword in condition_keywords):
                filtered.append(article)
        return filtered
