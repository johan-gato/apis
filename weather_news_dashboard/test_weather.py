from weather_service import obtener_clima

if __name__ == "__main__":
    ciudad = input("Ingrese una ciudad: ")
    clima = obtener_clima(ciudad)
    print("\n📊 Datos del Clima:")
    print(f"🌆 Ciudad: {clima['ciudad']}")
    print(f"🌡️ Temperatura: {clima['temperatura']} °C")
    print(f"💧 Humedad: {clima['humedad']}%")
    print(f"🌤️ Descripción: {clima['descripcion']}")
    print(f"💨 Viento: {clima['viento']} m/s")