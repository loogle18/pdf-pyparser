FROM python:3
MAINTAINER Sviat Minato

RUN mkdir /app
ADD main.py /app
RUN pip3 install pdfminer3k
ADD . /app

WORKDIR /app

ENTRYPOINT /bin/bash