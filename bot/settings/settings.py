from os import getenv
import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s %(message)s',
    filename='./log/msg.log',
    filemode='w',
    level=logging.INFO
)


TOKEN_BOT = getenv("TOKEN")

# Переменная определяет базу данных
# для разработки SQLite, для production PostgresSQL
ENV = "develop"
