import requests

class CountryService:
    def __init__(self):
        # Diccionario básico para obtener nombre de país desde código
        self.paises = {
            "cl": "Chile",
            "ar": "Argentina",
            "mx": "México",
            "us": "Estados Unidos",
            "co": "Colombia",
            "br": "Brasil"
        }

    def get_country_name(self, codigo):
        return self.paises.get(codigo.lower(), "Desconocido")

    def get_capital_by_country_code(self, codigo):
        nombre_pais = self.get_country_name(codigo)
        info = self.obtener_info_pais(nombre_pais)
        return info.get("capital")

    def obtener_info_pais(self, nombre_pais):
        url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
        respuesta = requests.get(url)

        if respuesta.status_code != 200:
            raise Exception(f"Error al obtener datos del país: {respuesta.status_code}")
        
        datos = respuesta.json()[0]
        resultado = {
            "nombre": datos["name"]["common"],
            "capital": datos["capital"][0],
            "poblacion": datos["population"],
            "moneda": list(datos["currencies"].keys())[0]
        }
        return resultado

# Bloque de prueba opcional
if __name__ == "__main__":
    pais = input("Ingresa el nombre del país (ej: Chile, Argentina): ").strip()
    try:
        servicio = CountryService()
        info = servicio.obtener_info_pais(pais)
        print("\nInformación del país:")
        for clave, valor in info.items():
            print(f"{clave.capitalize()}: {valor}")
    except Exception as e:
        print(f"❌ Error: {e}")
