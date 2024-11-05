import psycopg2

conexao = psycopg2.connect(
    dbname="projeto_csv",
    user="projeto_csv",
    password="projeto_csv",
    host="localhost",
    port="5432"
)

cursor = conexao.cursor()

cursor.execute('TRUNCATE TABLE pessoa')

conexao.commit()

cursor.close()
conexao.close()
