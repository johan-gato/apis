import requests
from config import OPENWEATHERMAP_API_KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric&lang=es"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "ciudad": data["name"],
            "temperatura": data["main"]["temp"],
            "descripcion": data["weather"][0]["description"]
        }
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    print(get_weather("La Serena"))