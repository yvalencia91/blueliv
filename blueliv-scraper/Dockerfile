FROM python:3.8.12-slim-buster
WORKDIR /usr/src/app
COPY . .

RUN pip install -r requirements.txt

ARG MYPASS=candidate
ENV PASSWD=${MYPASS}

ARG DEFAULT_HOST=localhost
ENV HOST=${DEFAULT_HOST}

CMD python main.py