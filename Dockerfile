FROM python:3.12-slim

ENV PYTHONPATH "${PYTHONPATH}:/flask-template"

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir -p /flask-template/project
COPY *.py .env /flask-template
COPY project /flask-template/project
WORKDIR /flask-template/project