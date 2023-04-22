#!/usr/bin/env python
import sys

from handler.start_polling import start_polling
from models.models import init_database, create_migrate

def migrate() -> None:
    """Обновление таблиц в БД."""
    create_migrate()
    print("Создание таблиц прошло успешно")

def runserver() -> None:
    """Запуск сервера."""
    init_database()
    start_polling()


def main() -> None:
    if len(sys.argv) <= 1:
        print("Введите аргумент один из возможных")
        return
    if sys.argv[1] == "migrate":
        migrate()
        return
    if sys.argv[1] == "runserver":
        runserver()
        return
    print("Введите доступные аргументы")


if __name__ == "__main__":
    main()
