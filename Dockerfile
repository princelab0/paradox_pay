FROM python:3-slim-buster
ENV PYTHONUNBUFFERED = 1
WORKDIR /payparadox
ADD . /payparadox

COPY ./requirements.txt /payparadox/requirements.txt
RUN pip install -r requirements.txt
COPY . /payparadox