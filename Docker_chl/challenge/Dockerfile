FROM python:3.12-slim

WORKDIR /app

RUN mkdir -p /app/logs
COPY app.py .
COPY requirements.txt .
COPY debug.log /app/logs/debug.log

RUN echo "flag{fake_flag}" > /app/admin_backup.txt
RUN echo "nothing interesting here" > /app/secrets.txt

RUN apt-get update && \
    apt-get install -y dnsutils curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
