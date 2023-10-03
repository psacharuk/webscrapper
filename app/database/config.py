import os

DB_USER = os.environ['DB_USER'] if 'DB_USER' in os.environ else 'root'
DB_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD'] if 'MYSQL_ROOT_PASSWORD' in os.environ else 'root'

DB_ADDRESS = os.environ['INTERNAL_DB_ADDRESS'] if 'INTERNAL_DB_ADDRESS' in os.environ else 'mysqldb'
DB_NAME = os.environ['DB_NAME'] if 'DB_NAME' in os.environ else 'webscrapper'

CONNECTION_STRING = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}'