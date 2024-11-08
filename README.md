# Processamento de arquivos CSV com técnicas em lote

Projeto que compara a eficiência de diferentes técnicas de processamento de arquivos csv para banco de dados.

<h2 id="tech">💻 Tecnologias</h2>

- Python
- Git
- Poetry
- Docker
- PostgreSQL
- Celery

## passo a passo para rodar o projeto.

- Clone o projeto localmente com o comando:
  ```bash
  git clone https://github.com/DerickDevCode/processamento_csv.git
  ```

- Instale as dependências usando poetry com o comando:
  ```bash
  poetry install
  ```

- Crie o seu arquivo .env e defina as variáveis de ambiente baseadas no arquivo env-sample:
  ```yaml
  POSTGRES_PASSWORD=defina sua senha do banco de dados aqui
  POSTGRES_USER=defina seu usuário do banco de dados aqui
  POSTGRES_DB=defina o nome do seu banco de dados aqui
  ```

- Após definir as variáveis de ambiente do Postgres acima, Suba um banco Postgresql e um Rabbitmq usando o
  docker-compose.yml:
  ```bash
  docker compose up
  ```

Agora você tem o projeto pronto para ser usado no seu computador.

Para gerar os arquivos com os dados para serem processados use o [criar_arquivos_csv.py](criar_arquivos_csv.py).

Os arquivos para configurar o processamento dos dados de forma síncrona são:

- [processar_dados_um_por_um.py](processar_dados_um_por_um.py)
- [processar_dados_em_lote.py](processar_dados_em_lote.py)
- [processar_dados_dois_arquivos_por_vez.py](processar_dados_dois_arquivos_por_vez.py)

As tasks para fazer o processamento assíncrono dos arquivos se encontram em [tasks.py](tasks.py) e você pode executá-las
rodando o arquivo [run_tasks.py](run_tasks.py)