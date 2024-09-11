FROM python:3.12-slim

ENV PYTHONPATH "${PYTHONPATH}:/brasa"

WORKDIR /project

COPY pyproject.toml *.env ./

RUN pip install .
