FROM python:3.8.12-slim-buster
EXPOSE 8000
WORKDIR /usr/src/app
COPY . .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install gcc -y && \
    pip install psutil && rm -rf /var/lib/apt/lists/*
RUN python create_tables.py

ARG JWT_KEY=blueliv-candidate-yohan-valencia
ARG DEFAULT_HOST=localhost
ENV APM_HOST = ${DEFAULT_HOST}
ENV KEY = ${JWT_KEY}


CMD gunicorn main:app -b 0.0.0.0:8000