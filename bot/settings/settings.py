import os
import logging
from dotenv import load_dotenv


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s %(message)s',
    filename='./log/msg.log',
    filemode='w',
    level=logging.INFO
)

# Переменная определяет базу данных
# для разработки SQLite, для production PostgresSQL
ENV = os.getenv("TOKEN", "develop")

if ENV == "develop":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

TOKEN_BOT = os.getenv("TOKEN")

DB_NAME = os.getenv('DB_NAME', default='postgres')
POSTGRES_USER = os.getenv('POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', default='postgres')
DB_HOST = os.getenv('DB_HOST', default='postgres')
DB_PORT = os.getenv('DB_PORT', default='5432')
