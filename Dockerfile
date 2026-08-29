# NexusCRM Enterprise Container Image
FROM python:3.12-slim

WORKDIR /app

# Install system utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || true

COPY . .

ENV PYTHONUNBUFFERED=1
ENV NEXUS_PORT=8080
ENV NEXUS_HOST=0.0.0.0

EXPOSE 8080

CMD ["python", "nexus/server.py"]
