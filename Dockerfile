FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY ZApplication /ZApplication
WORKDIR /ZApplication
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password z-user

USER z-user