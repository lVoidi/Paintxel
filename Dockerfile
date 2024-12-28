FROM python:3.12.2-slim

RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY backend.py .
COPY frontend.py .
COPY main.py .
COPY requirements.txt .
COPY PNGs/ ./PNGs/

RUN pip install --no-cache-dir -r requirements.txt

ENV DISPLAY=:0

CMD ["python", "main.py"]   