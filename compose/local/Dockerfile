FROM python:3.9

ARG PIP_INDEX_URL

ENV PIP_INDEX_URL=$PIP_INDEX_URL

RUN mkdir /app
RUN mkdir /app/static

WORKDIR /app

COPY ./requirements/requirements.txt ./requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]

RUN export $(grep -v '^#' .env | xargs)

COPY ./src/ /app/src/
COPY ./manage.py /app/