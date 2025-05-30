import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
print("API KEY:", api_key)

def test_top_headlines(country):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "country": country,
        "pageSize": 5
    }
    response = requests.get(url, params=params)
    print(f"\nTop headlines para país '{country}':")
    print("Status code:", response.status_code)
    print("Respuesta:", response.json())

def test_everything(query):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": api_key,
        "q": query,
        "pageSize": 5
    }
    response = requests.get(url, params=params)
    print(f"\nBúsqueda everything con término '{query}':")
    print("Status code:", response.status_code)
    print("Respuesta:", response.json())

if __name__ == "__main__":
    # Prueba con top headlines para US y AR (más probables que tengan noticias)
    test_top_headlines("us")
    test_top_headlines("ar")

    # Prueba con top headlines para Chile (puede devolver vacío)
    test_top_headlines("cl")

    # Prueba búsqueda general para Chile con everything
    test_everything("Chile")