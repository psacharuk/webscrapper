FROM python:alpine3.18

# required by mysqlclient
RUN apk --no-cache add mariadb-dev build-base
COPY pip-requirements.txt .

RUN pip install --no-cache-dir -r pip-requirements.txt

COPY . .

ARG FASTAPI_PORT
ARG SERVER_IP

EXPOSE $FASTAPI_PORT
CMD uvicorn app.main:fastapi_app --host ${SERVER_IP} --port ${FASTAPI_PORT} --reload

