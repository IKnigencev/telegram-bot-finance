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
    DecimalField,
    PostgresqlDatabase,
    SqliteDatabase
)

from settings.settings import (
    ENV,
    DB_NAME,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    DB_HOST,
    DB_PORT
)

if ENV == "develop":
    db = SqliteDatabase(
        "./dev.db"
    )
else:
    db = PostgresqlDatabase(
        DB_NAME,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
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

    def __str__(self) -> str:
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

    def __str__(self) -> str:
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

    def __str__(self) -> str:
        return self.sum_transaction


def create_migrate() -> None:
    db.connect()
    db.create_tables([User, BalanceModels, TransactionModels])


def init_database() -> None:
    db.connect()
    db.rollback()
