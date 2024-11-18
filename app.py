"""
app.py

Crea la aplicación Flask y define las rutas para la consulta del clima.
"""

from flask import Flask, render_template, request
from clima import obtener_clima

# Crea la instancia de la aplicación Flask
app = Flask(__name__)

# Define la ruta raíz de la aplicación, que muestra un mensaje de bienvenida
@app.route('/')
def index():
    return render_template('index.html')

# Define la ruta para la consulta del clima
@app.route('/weather', methods=['POST'])
def weather():
    """
    Obtiene el clima de una ciudad y las unidades de medida.
    :return: Devuelve una plantilla HTML con los resultados del clima.
    """

    # Obtiene los datos de la petición POST y obtiene la ciudad y las unidades de medida.
    ciudad = request.form['city']
    units = request.form['units']

    # Obtiene el clima de la ciudad y las unidades de medida. Si la ciudad no es encontrada, muestra un error.
    clima_data = obtener_clima(ciudad, units)
    if clima_data is None:
        return render_template('index.html', error='Ciudad no encontrada')
    else:
        return render_template('weather.html', ciudad=ciudad, clima=clima_data, units=units)

# Ejecuta la aplicación en el puerto 5000. El argumento debug=True habilita la depuración de la aplicación.
if __name__ == '__main__':
    """
    Este código se ejecuta cuando se ejecuta este script directamente. En caso de ser importado como un módulo, 
    este código no se ejecuta.
    Este script se encarga de inicializar la aplicación Flask y exponerla en el puerto 5000.
    """
    app.run(port=5000, debug=True)
