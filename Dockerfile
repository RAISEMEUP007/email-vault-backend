FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 5000

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
