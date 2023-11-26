from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['PGSQL_USER']
host = os.environ['PGSQL_HOST']
password = os.environ['PGSQL_PASSWORD']
database = os.environ['PGSQL_DATABASE']
port = os.environ['PGSQL_PORT']

SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'