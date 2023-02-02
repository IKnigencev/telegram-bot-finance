import datetime

from peewee import (
    Model,
    IntegerField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    SqliteDatabase
)


db = SqliteDatabase('my_project.db')


class MixinConfig(Model):
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        order_by = ('-created',)


class User(MixinConfig):
    id_telegram = IntegerField(unique=True, index=True)
    name = CharField(max_length=100)
    last_name = CharField(max_length=150)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name


class TransactionModels(MixinConfig):
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
