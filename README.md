# Aplicación del Clima

Esta es una aplicación web simple que permite a los usuarios consultar el clima actual de una ciudad específica. La aplicación utiliza la API de OpenWeatherMap para obtener los datos del clima y muestra la información en un formato amigable para el usuario.

## Características

- Consulta el clima actual de cualquier ciudad.
- Muestra la temperatura, sensación térmica, temperatura máxima y mínima, presión atmosférica, velocidad del viento, humedad y descripción del clima.
- Permite al usuario elegir entre dos sistemas de medición: Métrico (°C, Km/h) y Americano (°F, mph).
- Muestra un mensaje de error si la ciudad no se encuentra.

## Tecnologías Utilizadas

- **Flask**: Framework de Python para el desarrollo web.
- **OpenWeatherMap API**: API para obtener datos del clima.
- **Bootstrap**: Framework de CSS para el diseño y la interfaz de usuario.
- **FontAwesome**: Biblioteca de iconos para mejorar la interfaz de usuario.

## Estructura del Proyecto
/app
│
├── app.py # Archivo principal de la aplicación Flask
├── clima.py # Módulo para obtener datos del clima desde OpenWeatherMap
├── templates/
│ ├── index.html # Plantilla para la página de inicio
│ └── weather.html # Plantilla para mostrar los datos del clima
├── static/
│ └── CSS/
│ └── style.css # Archivo de estilos CSS
└── README.md # Documentación del proyecto

Copy

## Instalación y Ejecución

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/aplicacion-del-clima.git
   cd aplicacion-del-clima
Instala las dependencias:

bash
Copy
pip install -r requirements.txt
Configura la API Key de OpenWeatherMap:

Obtén una API Key desde OpenWeatherMap.

Reemplaza la API Key en el archivo clima.py:

python
Copy
api_key = 'TU_API_KEY'
Ejecuta la aplicación:

bash
Copy
python app.py
Accede a la aplicación:
Abre tu navegador web y visita http://127.0.0.1:5000/.

Uso
Ingresa el nombre de la ciudad en el campo proporcionado.

Selecciona el sistema de medición (Métrico o Americano).

Haz clic en el botón "Consultar Clima".

Los datos del clima se mostrarán en la página.
