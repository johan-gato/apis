import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

class NewsService:
    def __init__(self, pais="Chile"):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2"
        self.pais = pais
        if not self.api_key:
            raise ValueError("NEWS_API_KEY no está configurada en .env")

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        logging.error(f"Error {response.status_code}: {response.text}")
        return None

    def get_country_code(self, nombre_pais):
        codigos = {
            "chile": "cl",
            "argentina": "ar",
            "mexico": "mx",
            "colombia": "co",
            "brasil": "br",
            "estados unidos": "us"
        }
        return codigos.get(nombre_pais.lower(), "us")  # Por defecto usa "us"

    def get_top_headlines(self, country="us", category=None, page=1, page_size=20):
        country_code = self.get_country_code(self.pais)
        url = f"{self.base_url}/top-headlines"
        params = {
            "apiKey": self.api_key,
            "country": country_code,
            "page": page,
            "pageSize": page_size
        }
        if category:
            params["category"] = category

        response = requests.get(url, params=params)
        return self._handle_response(response)

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

    def resumen_noticias(self):
        datos = self.get_top_headlines()
        if not datos or not datos.get("articles"):
            return "No se encontraron noticias."
        
        resumen = ""
        for i, noticia in enumerate(datos["articles"][:5], 1):
            titulo = noticia.get("title", "Sin título")
            fuente = noticia.get("source", {}).get("name", "Fuente desconocida")
            resumen += f"{i}. {titulo} ({fuente})\n"
        return resumen
