from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configura los detalles de la conexión a la base de datos
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'coreacmm',
    'auth_plugin': 'mysql_native_password'
}

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # Establece la conexión con la base de datos
        conn = mysql.connector.connect(**db_config)

        # Crea un cursor para ejecutar consultas SQL
        cursor = conn.cursor()

        # Ejecuta una consulta SQL para obtener los datos
        query = 'SELECT * FROM products'
        cursor.execute(query)

        # Obtiene los resultados de la consulta
        data = cursor.fetchall()

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

        # Convierte los resultados a un formato JSON y los devuelve en la respuesta de la API
        response = jsonify(data)
        return response

    except mysql.connector.Error as error:
        # Maneja cualquier error de conexión o consulta SQL
        print(f'Error al conectar a la base de datos: {error}')
        return jsonify({'error': 'Error al obtener los datos de la base de datos'})

if __name__ == '__main__':
    app.run()
