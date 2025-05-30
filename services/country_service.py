import requests

def get_country_info(country):
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        return {
            "nombre": data["name"]["common"],
            "capital": data["capital"][0],
            "poblacion": data["population"],
            "bandera": data["flags"]["png"]
        }
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    print(get_country_info("Chile"))