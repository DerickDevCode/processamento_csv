<h1 align="center" style="font-weight: bold;">Processamento de arquivos CSV com técnicas em lote</h1>

Projeto que compara a eficiência de diferentes técnicas de processamento de arquivos csv para banco de dados.

<h2 id="tech">💻 Tecnologias</h2>

- Python
- Git
- Poetry
- Docker
- PostgreSQL
- Celery

## Passo a passo para rodar o projeto.

Clone o projeto localmente com o comando:

  ```bash
  git clone https://github.com/DerickDevCode/processamento_csv.git
  ```

### Instale as dependências usando poetry.

Caso não tenha o Poetry instalado, instale-o com o comando:

  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

Com o Poetry instalado, instale as dependências com o comando:

  ```bash
  poetry install
  ```

### Crie o seu arquivo .env e defina as variáveis de ambiente baseadas no arquivo env-sample:

  ```yaml
  POSTGRES_PASSWORD=defina sua senha do banco de dados aqui
  POSTGRES_USER=defina seu usuário do banco de dados aqui
  POSTGRES_DB=defina o nome do seu banco de dados aqui
  ```

### Configurando o banco de dados PostgreSQL e o message broker RabbitMQ.

Após definir as variáveis de ambiente do PostgreSQL acima, suba um banco PostgreSQL e um RabbitMQ usando o
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
