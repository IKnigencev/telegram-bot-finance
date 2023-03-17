"""Файл для работы с бд и моделями.

- Создание таблиц в бд;
- Подключение к бд;
- Определение основных моделей бд;
"""
import os
import datetime

from peewee import (
    Model,
    IntegerField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    DecimalField,
    PostgresqlDatabase
)


db = PostgresqlDatabase(
    os.getenv('DB_NAME', default='postgres'),
    user=os.getenv('POSTGRES_USER', default='postgres'),
    password=os.getenv('POSTGRES_PASSWORD', default='postgres'),
    host=os.getenv('DB_HOST', default='postgres'),
    port=os.getenv('DB_PORT', default='5432')
)


CURRENCY_TYPE = (
    ("ru", "рубль")
)


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


class BalanceModels(MixinConfig):
    """Класс сохранения баланса клиента"""
    user = ForeignKeyField(
        User,
        unique=True,
        related_name='balance'
    )
    money = DecimalField(
        max_digits=19,
        decimal_places=2,
        auto_round=True,
        default=0
    )
    currency = CharField(
        max_length=3,
        choices=CURRENCY_TYPE,
        default="ru"
    )

    class Meta:
        db_table = 'balance'

    def __str__(self):
        return f"{self.user.id} - {self.money}"


class TransactionModels(MixinConfig):
    """Класс сохранения транзакций"""
    TYPE_TRANSACTION = (
        ('-', 'Удаление'),
        ('+', 'Добавление')
    )

    balance = ForeignKeyField(BalanceModels, related_name="transactions")
    type_transaction = CharField(choices=TYPE_TRANSACTION)
    sum_transaction = DecimalField(
        max_digits=19,
        decimal_places=2,
        auto_round=True,
        default=0
    )
    currency = CharField(
        max_length=3,
        choices=CURRENCY_TYPE,
        default="ru"
    )

    class Meta:
        db_table = 'transaction'

    def __str__(self):
        return self.sum_transaction


def create_migrate():
    db.connect()
    db.create_tables([User, BalanceModels, TransactionModels])


def init_database():
    db.connect()
    db.rollback()
