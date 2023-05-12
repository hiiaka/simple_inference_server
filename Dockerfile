FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /app

ENTRYPOINT ["python", "inference.py"]
