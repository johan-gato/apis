import requests
from weather_news_dashboard.gmail_service import enviar_reporte
import time

# API KEYS
weather_key = "TU_API_KEY_OPENWEATHER"
news_key = "TU_API_KEY_NEWSAPI"

pais = input("Ingresa un país: ")

# === REST Countries ===
datos_pais = requests.get(f"https://restcountries.com/v3.1/name/{pais}").json()[0]
capital = datos_pais["capital"][0]
codigo_pais = datos_pais["cca2"].lower()

# === Clima ===
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={capital}&appid={weather_key}&units=metric&lang=es"
clima = requests.get(weather_url).json()
info_clima = f"Clima en {capital}:\n{clima['weather'][0]['description'].capitalize()}, {clima['main']['temp']}°C"

# === Noticias ===
news_url = f"https://newsapi.org/v2/top-headlines?country={codigo_pais}&apiKey={news_key}"
noticias = requests.get(news_url).json()
titulares = "\n".join([f"- {n['title']}" for n in noticias["articles"][:5]])
info_noticias = f"\nNoticias recientes de {pais}:\n{titulares}"

# === Reporte final ===
reporte = f"{info_clima}\n\n{info_noticias}"

# === Espera 5 minutos y envía por Gmail ===
print("Esperando 5 minutos para enviar el correo...")
time.sleep(300)  # 5 minutos
enviar_reporte(
    destinatario="destinatario@correo.com",
    asunto=f"Reporte diario de {capital}, {pais}",
    cuerpo=reporte,
    remitente="tu_correo@gmail.com",
    clave_app="tu_clave_app_gmail"
)