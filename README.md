# Dashboard Clima y Noticias - Configuración de Servicios

## Instrucciones para ejecutar

1. Clona el proyecto y cambia a tu rama:
   ```bash
   git clone ...
   git checkout configuracion-servicios

2. Crea el entorno virtual:
   python -m venv venv
    venv\Scripts\activate

3. Copia .env.example a .env y agrega tus  
   claves

4. Instala las dependencias:
    pip install -r requirements.txt

5. Ejecuta:
   python services/weather_service.py
   python services/country_service.py