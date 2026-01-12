FROM python:3.10-slim

WORKDIR /app

COPY src/ src/
COPY tst/ tst/

RUN pip install --upgrade pip \
    && pip install typer colorlog pytest

ENV PYTHONPATH=/app/src

CMD ["python", "-m", "calculator_service", "--help"]
