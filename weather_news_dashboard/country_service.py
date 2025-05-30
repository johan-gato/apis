import requests

def obtener_info_pais(nombre_pais):
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
