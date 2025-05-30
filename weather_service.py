import requests
from config import OPENWEATHERMAP_API_KEY

def obtener_clima(ciudad):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={OPENWEATHERMAP_API_KEY}&units=metric&lang=es"
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
