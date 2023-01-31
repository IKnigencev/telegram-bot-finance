import os
from os.path import join, dirname
from dotenv import load_dotenv
import logging


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logging.basicConfig(filename='../log/msg.log', filemode='a', level=logging.INFO)


TOKEN_BOT = os.environ.get("TOKEN")


def logger(level:int, text:str) -> None:
    logging.level(text)
