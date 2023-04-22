#!/usr/bin/env python
import sys

from handler.start_polling import start_polling
from models.models import init_database, create_migrate


def main():
    if len(sys.argv) <= 1:
        print("Введите аргумент один из возможных")
        return None
    if sys.argv[1] == "migrate":
        create_migrate()
        print("Создание таблиц прошло успешно")
        return None
    if sys.argv[1] == "runserver":
        init_database()
        start_polling()
        return None
    print("Введите доступные аргументы")


if __name__ == "__main__":
    main()
