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

with open('arquivo1.csv', 'r') as arquivo:
    reader = csv.reader(arquivo)
    next(reader)
    tamanho_lote = 10000
    lote = []

    inicio = time.perf_counter()

    for linha in reader:
        lote.append(linha)

        if len(lote) == tamanho_lote:
            cursor.executemany(
                'INSERT INTO pessoa (nome, idade, cidade) VALUES (%s, %s, %s)', lote
            )
            conexao.commit()
            lote = []

    if lote:
        cursor.executemany(
            'INSERT INTO pessoa (nome, idade, cidade) VALUES (%s, %s, %s)', lote
        )
        conexao.commit()

    fim = time.perf_counter()

    tempo_total = fim - inicio
    print(f'{tempo_total:.2f}')

cursor.close()
conexao.close()
