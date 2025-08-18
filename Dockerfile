FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --upgrade pip wheel \
    && pip install "poetry==2.1.1" \
    && poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install --only main --no-interaction --no-ansi

COPY fastapi_app .

RUN chmod +x prestart.sh

ENTRYPOINT ["./prestart.sh"]

CMD ["gunicorn", "main:main_app", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "--bind", "0.0.0.0:8000"]
