import csv
import time

import psycopg2
from celery import Celery
from decouple import config

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')


@app.task
def processar_dados_em_lote(arquivo):
    conexao = psycopg2.connect(
        dbname=config('POSTGRES_DB'),
        user=config('POSTGRES_USER'),
        password=config('POSTGRES_PASSWORD'),
        host="localhost",
        port="5432"
    )

    cursor = conexao.cursor()

    with open(arquivo, 'r') as arquivo:
        reader = csv.reader(arquivo)
        next(reader)
        tamanho_lote = 2000
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

    cursor.close()
    conexao.close()

    return tempo_total


@app.task
def processar_dados_um_por_um(arquivo):
    conexao = psycopg2.connect(
        dbname=config('POSTGRES_DB'),
        user=config('POSTGRES_USER'),
        password=config('POSTGRES_PASSWORD'),
        host="localhost",
        port="5432"
    )

    cursor = conexao.cursor()

    with open(arquivo, 'r', newline='') as arquivo:
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

    cursor.close()
    conexao.close()

    return tempo_total


@app.task
def processar_dados_varios_arquivos_por_vez(*arquivos):
    inicio = time.perf_counter()

    for arq in arquivos:
        processar_dados_em_lote.delay(arq)

    fim = time.perf_counter()
    tempo_total = fim - inicio

    return tempo_total
