FROM python:alpine3.18

# required by mysqlclient
RUN apk --no-cache add mariadb-dev build-base
COPY pip-requirements.txt .

RUN pip install --no-cache-dir -r pip-requirements.txt

COPY . .
# to env variable
EXPOSE 9000

CMD ["uvicorn", "app.main:fastapi_app", "--host", "0.0.0.0", "--port", "9000", "--reload"]


