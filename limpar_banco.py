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

cursor.execute('TRUNCATE TABLE pessoa')

conexao.commit()

cursor.close()
conexao.close()
