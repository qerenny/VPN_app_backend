FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
COPY src/vpn_backend /app/vpn_backend


RUN pip install poetry
RUN poetry install --no-root

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "vpn_backend.main:app", "--host", "0.0.0.0", "--port", "8000"]