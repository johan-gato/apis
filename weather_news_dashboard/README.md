# Weather & News Dashboard 🌦️📰

Una aplicación en Python que permite consultar noticias recientes por país utilizando la API de NewsAPI.

## 🚀 Características

- Obtener titulares principales (`top-headlines`) por país.
- Si no hay titulares, buscar artículos usando el nombre del país como término de búsqueda.
- Interfaz por consola sencilla.
- Configuración segura de claves API con `.env`.

## 📁 Estructura del Proyecto


## ⚙️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/weather_news_dashboard.git
cd weather_news_dashboard

#Creacion entorno virtual(Opcional)

python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows


dependencia
pip install -r requirements.txt

crear .env y agregar key
NEWS_API_KEY=tu_api_key_aquí

ejecucion
python -m weather_news_dashboard.test

🧰 Tecnologías
Python 3.9+

NewsAPI.org

requests

python-dotenv

📌 Notas
Asegúrate de no subir el archivo .env a ningún repositorio público.

El proyecto está diseñado para ser fácilmente expandido a futuras integraciones como clima, exportación JSON o envío de reportes por correo.

📜 Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT.


---

## ✅ 2. `.gitignore`

Asegúrate de que este archivo esté en la raíz del proyecto para evitar subir archivos no deseados:

```gitignore
# Entorno virtual
venv/
.env

# Archivos Python
__pycache__/
*.pyc

# Archivos de sistema
.DS_Store
Thumbs.db

