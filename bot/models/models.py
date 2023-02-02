"""Файл для работы с бд и моделями.

- Создание таблиц в бд;
- Подключение к бд;
- Определение основных моделей бд;
"""
import datetime

from peewee import (
    Model,
    IntegerField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    PostgresqlDatabase,
    SqliteDatabase
)

from settings.settings import ENV

if ENV == "develop":
    db = SqliteDatabase('./bot/my_project.db')
else:
    db = PostgresqlDatabase()


class MixinConfig(Model):
    """Общий класс моделей"""
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        order_by = ('-created',)


class User(MixinConfig):
    """Класс сохранения юзеров"""

    id_telegram = IntegerField(unique=True, index=True)
    name = CharField(max_length=100)
    last_name = CharField(max_length=150)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name


class TransactionModels(MixinConfig):
    """Класс сохранения транзакций"""

    user = ForeignKeyField(User, to_field='id')
    type_transaction = CharField()
    sum_transaction = IntegerField()

    class Meta:
        db_table = 'transaction'


def create_migrate():
    db.connect()
    db.create_tables([User, TransactionModels])
    db.close()


def init_database():
    db.connect()
