import csv
import time

import psycopg2
from decouple import config

conexao = psycopg2.connect(
    dbname=config('POSTGRES_DB'),
    user=config('POSTGRES_USER'),
    password=config('POSTGRES_PASSWORD'),
    host="localhost",
    port="5432"
)

cursor = conexao.cursor()

with open('arquivo1.csv', 'r', newline='') as arquivo:
    reader = csv.reader(arquivo)
    next(reader)
    lote = []

    inicio = time.perf_counter()

    for linha in reader:
        lote.append(linha)
        cursor.executemany(
            'INSERT INTO pessoa (nome, idade, cidade) VALUES (%s, %s, %s)', lote
        )
        conexao.commit()
        lote = []

    fim = time.perf_counter()

tempo_total = fim - inicio
print(tempo_total)

cursor.close()
conexao.close()