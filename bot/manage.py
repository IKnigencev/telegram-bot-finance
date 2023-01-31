#!/usr/bin/env python
import sys

from handler.start_polling import start_polling
from models.models import init_database



def main():
    if len(sys.argv) <= 1:
        print("Введите аргумент один из возможных")
        return None
    match sys.argv[1]:
        case "migrate":
            init_database()
            print("Создание таблиц прошло успешно")
        case "runserver":
            start_polling()
        case _:
            print("Введите доступные аргументы")


if __name__ == "__main__":
    main()
