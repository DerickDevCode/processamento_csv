ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"
ENV POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --no-dev

COPY . /app

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "docker_e_poetry.wsgi"]
