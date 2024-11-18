"""
clima.py

Este módulo contiene funciones para obtener el clima de ciudades utilizando la API de OpenWeatherMap.

"""

import requests

def obtener_clima(ciudad, units='metric'):
    """
    Devuelve la temperatura actual en grados Celsius de la ciudad pasada como argumento.

    Args:
        ciudad (str): Nombre de la ciudad.
        units (str): Sistema de medición ('metric' para Celsius, 'imperial' para Fahrenheit).
    Returns:
        dict: Diccionario con la temperatura, la temperatura maxima, la temperatura minima,
        la presion, la velocidad del viento, la humedad y la descripcion del clima.
    """
    # Creamos la URL base de la API de OpenWeatherMap.
    base_url = f"http://api.openweathermap.org/data/2.5/weather?"
    # Agregamos la clave de la API de OpenWeatherMap al URL.
    api_key = '3796934179af73efc7d5213b80cda195'
    # Agregamos la API key al URL para obtener los datos del clima.
    # El parámetro 'lang' se utiliza para especificar el idioma de la respuesta.
    # El parámetro 'units' se utiliza para especificar la unidad de medida (metric, imperial o standard).
    full_url = f"{base_url}q={ciudad}&lang=es&appid={api_key}&units={units}"
     # Realizamos la peticion HTTP y obtenemos la respuesta.
    response = requests.get(full_url)

    if response.status_code == 200:
        # 200 es el codigo de respuesta correcto de la peticion HTTP y 404 es el codigo de error.

        # Obtenemos los datos del clima del JSON de la respuesta.
        data = response.json()
        # Obtenemos los datos principales del clima.
        main = data['main']
        # Obtenemos los datos del viento.
        wind = data['wind']
        # Obtenemos la descripción del clima.
        weather_description = data['weather'][0]['description']

        # Convertir presión de hPa a inHg si el sistema de medición es imperial
        presion = main['pressure']
        if units == 'imperial':
            presion = round(presion * 0.02953, 2)

        # Convertir velocidad del viento de m/s a Km/h si el sistema de medición es metric
        velocidad_viento = wind['speed']
        if units == 'metric':
            velocidad_viento = round(velocidad_viento * 3.6, 2)

        # Devolvemos el diccionario con los datos del clima.
        return {
            'temperatura': main['temp'],
            'temperatura_maxima': main['temp_max'],
            'temperatura_minima': main['temp_min'],
            'sensacion_termica': main['feels_like'],
            'presion': presion,
            'velocidad_viento': velocidad_viento,
            'humedad': main['humidity'],
            'descripcion': weather_description,
        }
    else:
        return None

# Ejemplo de uso:
"""
# Obtenemos el clima de Buenos Aires.
weather = obtener_clima('Buenos Aires')
print(weather)
"""

