import requests
from config import OPENWEATHERMAP_API_KEY

class WeatherService:
    def __init__(self):
        self.api_key = OPENWEATHERMAP_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, ciudad):
        url = f"{self.base_url}?q={ciudad}&appid={self.api_key}&units=metric&lang=es"
        respuesta = requests.get(url)
        
        if respuesta.status_code != 200:
            raise Exception(f"Error al obtener clima: {respuesta.status_code}")
        
        datos = respuesta.json()
        resultado = {
            "ciudad": datos["name"],
            "temperatura": datos["main"]["temp"],
            "humedad": datos["main"]["humidity"],
            "descripcion": datos["weather"][0]["description"],
            "viento": datos["wind"]["speed"]
        }
        return resultado
