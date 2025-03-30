from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return connection

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()  

    if len(query) > 255:
        return jsonify({"error": "A query é muito longa. Máximo permitido: 255 caracteres."}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT registro_ans, cnpj, razao_social, nome_fantasia, modalidade, cidade, uf
        FROM operadoras_plano_saude
        WHERE razao_social LIKE %s OR nome_fantasia LIKE %s
        ORDER BY razao_social ASC
        LIMIT 10
    """, ('%' + query + '%', '%' + query + '%'))

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
