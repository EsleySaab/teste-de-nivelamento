import csv
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

cursor = conn.cursor()

file_path = 'banco_de_dados/4T2024.csv'  

with open(file_path, newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=';')
    next(csv_reader)  

    for row in csv_reader:
        vl_saldo_inicial = row[4].replace(',', '.') if row[4] else '0'
        vl_saldo_final = row[5].replace(',', '.') if row[5] else '0'

        cursor.execute("""
            INSERT INTO despesas_operadoras (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (row[0], row[1], row[2], row[3], vl_saldo_inicial, vl_saldo_final))

conn.commit()
cursor.close()
conn.close()
