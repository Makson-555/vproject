FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /vproject

WORKDIR /vproject

COPY requirements.txt /vproject/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /vproject/