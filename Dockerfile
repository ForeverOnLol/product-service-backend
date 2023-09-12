FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/dd_test

COPY ./req.txt /usr/src/req.txt

RUN pip install -r /usr/src/req.txt

