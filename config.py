import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Validaciones opcionales
if not OPENWEATHERMAP_API_KEY:
    raise ValueError("Falta configurar OPENWEATHERMAP_API_KEY en el archivo .env")

if not NEWS_API_KEY:
    raise ValueError("Falta configurar NEWS_API_KEY en el archivo .env")
