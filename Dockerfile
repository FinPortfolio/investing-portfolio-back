FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --upgrade pip wheel \
    && pip install "poetry==2.1.1" \
    && poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install --only main --no-interaction --no-ansi

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
