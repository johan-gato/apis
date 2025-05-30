import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables desde .env

api_key = os.getenv("NEWS_API_KEY")

if api_key:
    print(f"La API key es: {api_key}")
else:
    print("No se encontró la variable NEWS_API_KEY en .env")