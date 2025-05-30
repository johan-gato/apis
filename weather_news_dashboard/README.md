# 🌦️ Weather News Dashboard

Proyecto de integración de APIs que permite visualizar información meteorológica y noticias recientes según el país seleccionado. Utiliza OpenWeatherMap, NewsAPI y REST Countries, y genera un reporte diario en formato JSON.

---

## 🧑‍💻 Integrantes

- Integrante 1: [Johan] – Clima y servicio REST Countries  
- Integrante 2: [Mauricio] – Noticias, Dashboard y Git**  
- Integrante 3: [David] – Reportes JSON, Gmail API y validación  

---

## 🧰 Tecnologías y Librerías

- Python 3.x  
- `requests`  
- `python-dotenv`  
- `smtplib` (para envío de correo)  
- `json`, `os`, `datetime`  
- APIs: OpenWeatherMap, NewsAPI, REST Countries, Gmail API  

---

## 📦 Estructura del Proyecto

weather_news_dashboard/
├── main.py
├── config.py
├── weather_service.py
├── news_service.py
├── country_service.py
├── dashboard.py
├── reporte_diario.json
├── .env
├── .gitignore
└── requirements.txt



---

## 🌍 APIs Utilizadas

| API             | Función                          | URL                                               |
|-----------------|---------------------------------|--------------------------------------------------|
| NewsAPI         | Obtener titulares y noticias     | https://newsapi.org                              |
| OpenWeatherMap  | Clima actual                    | https://openweathermap.org/api                   |
| REST Countries  | Información de países            | https://restcountries.com                         |
| Gmail API       | Envío automático de correos      | https://developers.google.com/gmail/api          |

---

## ⚙️ Instrucciones de Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/weather_news_dashboard.git
   cd weather_news_dashboard


## Crear y activar entorno virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows PowerShell

## Instalar dependencias:
pip install -r requirements.txt

## Crear archivo .env en la raíz con tus claves API
NEWS_API_KEY=tu_clave_newsapi
OPENWEATHERMAP_API_KEY=tu-clave
WEATHER_API_KEY=tu_clave_openweathermap
EMAIL_ADDRESS=correo_del_grupo@gmail.com
EMAIL_PASSWORD=clave_o_contraseña_de_aplicacion

## 🚀 Uso
python weather_service.py
python country_service.py

python main.py
python -m weather_news_dashboard.test_news

## 📤 Salida del Programa
Información meteorológica y noticias por consola.

Archivo reporte_diario.json con resumen del día.

(Opcional) Envío de correo con los datos — pendiente por implementar.



