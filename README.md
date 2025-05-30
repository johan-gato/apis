# Weather News Dashboard

## Descripción

`weather_news_dashboard` es una aplicación en Python que combina información meteorológica y noticias relevantes para un país seleccionado, generando un reporte diario. Este reporte se muestra por consola, se guarda en formato JSON y texto plano, y ofrece una correlación inteligente entre el clima actual y noticias relacionadas.

## Funcionalidades

- Consulta el clima actual de la capital de un país ingresado.
- Obtiene las principales noticias del país, o noticias relacionadas si no hay titulares destacados.
- Correlaciona noticias relevantes con la descripción del clima.
- Genera un reporte diario combinando clima y noticias.
- Exporta el reporte a archivos JSON y TXT.
- Interfaz sencilla de línea de comandos.

## Requisitos

- Python 3.7+
- Paquetes Python: `requests`, `python-dotenv`
- Claves API necesarias:
  - **OpenWeatherMap API Key** (para datos meteorológicos)
  - **NewsAPI Key** (para noticias)
- Archivo `.env` con las variables de entorno:

OPENWEATHERMAP_API_KEY=tu_api_key_aqui
NEWS_API_KEY=tu_api_key_aqui


## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/weather_news_dashboard.git
cd weather_news_dashboard/apis

## Crea y activa un entorno virtual:
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

## Instalar dependencias:
pip install -r requirements.txt

## Constraseñas:
Crea el archivo .env con tus claves de API en la misma carpeta del código.

## Uso
## Ejecuta el dashboard desde la terminal:
python dashboard.py

Se solicitará el código ISO del país (ejemplo: cl para Chile, us para Estados Unidos).
El programa mostrará un reporte diario en consola y generará los archivos:
reporte_diario.json
reporte_diario.txt

weather_news_dashboard/
├── apis/
│   ├── dashboard.py
│   ├── news_service.py
│   ├── weather_service.py
│   ├── country_service.py
│   ├── config.py
│   ├── requirements.txt
│   └── .env
└── README.md

## API Keys
OpenWeatherMap: https://openweathermap.org/api
NewsAPI: https://newsapi.org/

Obtén tus claves gratuitas registrándote en cada servicio.

---
## ✅ requirements.txt (contenido para copiar)

```txt
requests
python-dotenv

