# 🌦️ Weather News Dashboard

Proyecto de integración de APIs que permite visualizar información meteorológica y noticias recientes según el país seleccionado. Utiliza OpenWeatherMap, NewsAPI y REST Countries. También genera un reporte diario en formato JSON.

---

## 🧑‍💻 Integrantes

- Integrante 1: [Nombre] – Clima y servicio REST Countries
- **Integrante 2: [Tu nombre] – Noticias, Dashboard y Git**
- Integrante 3: [Nombre] – Reportes JSON, Gmail API y validación

---

## 🧰 Tecnologías y Librerías

- Python 3.x
- `requests`
- `python-dotenv`
- `smtplib` (para correo)
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

| API             | Función                          | URL                             |
|----------------|----------------------------------|---------------------------------|
| NewsAPI        | Obtener titulares y noticias     | https://newsapi.org             |
| OpenWeatherMap | Clima actual                     | https://openweathermap.org/api  |
| REST Countries | Información de países            | https://restcountries.com       |
| Gmail API      | Envío automático de correos      | https://developers.google.com/gmail/api |

---

## ⚙️ Instrucciones de Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/weather_news_dashboard.git
   cd weather_news_dashboard

## Crear entorno virtual

python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows

## Instalar dependencias

pip install -r requirements.txt


## Crear archivo .env con claves
#NEWS_API_KEY=tu_clave_newsapi
#WEATHER_API_KEY=tu_clave_openweathermap


## Ejecucion

python main.py
python -m weather_news_dashboard.test

📤 Salida del Programa
Muestra información del clima y noticias en consola.

Guarda un archivo reporte_diario.json con el resumen.

Opcionalmente envía un correo con los datos.

🗂️ Estado del Proyecto
✅ Módulo noticias (news_service.py)
✅ Dashboard funcional (dashboard.py)
✅ Configuración Git y estructura lista
🔄 En integración con módulos de clima y correo

💡 Créditos
Hecho por estudiantes de INACAP para la evaluación 2.1.2.1 – Integración de APIs.








# 🌦️ Weather News Dashboard

Proyecto de integración de APIs que permite visualizar información meteorológica y noticias recientes según el país seleccionado. Utiliza OpenWeatherMap, NewsAPI y REST Countries, y genera un reporte diario en formato JSON.

---

## 🧑‍💻 Integrantes

- Integrante 1: [Nombre] – Clima y servicio REST Countries  
- **Integrante 2: [Tu nombre] – Noticias, Dashboard y Git**  
- Integrante 3: [Nombre] – Reportes JSON, Gmail API y validación  

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


#Crear y activar entorno virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows PowerShell

#Instalar dependencias:
pip install -r requirements.txt

#Crear archivo .env en la raíz con tus claves API
NEWS_API_KEY=tu_clave_newsapi
WEATHER_API_KEY=tu_clave_openweathermap

🚀 Uso
python main.py

📤 Salida del Programa
Información meteorológica y noticias por consola.

Archivo reporte_diario.json con resumen del día.

(Opcional) Envío de correo con los datos — pendiente por implementar.

🗂️ Estado del Proyecto
✅ Módulo de noticias (news_service.py)

✅ Dashboard funcional (dashboard.py)

✅ Configuración Git y estructura organizada

🔄 Integración en proceso con módulos de clima y correo


