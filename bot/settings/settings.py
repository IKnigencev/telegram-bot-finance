import os
from os.path import join, dirname
from dotenv import load_dotenv
import logging


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logging.basicConfig(
    format='%(levelname)s:%(message)s',
    filename='./log/msg.log',
    filemode='w',
    level=logging.INFO
)


TOKEN_BOT = os.environ.get("TOKEN")

# Переменная определяет базу данных
# для разработки SQLite, для production PostgresSQL
ENV = "develop"
