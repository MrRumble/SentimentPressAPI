FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["python", "run.py"]
