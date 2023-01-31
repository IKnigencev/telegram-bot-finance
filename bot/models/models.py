import datetime

from peewee import (
    Model,
    IntegerField,
    CharField,
    DateTimeField,
    SqliteDatabase
)


db = SqliteDatabase("my_project.db")


class MixinConfig(Model):
    class Meta:
        database = db


class User(MixinConfig):
    id_telegram = IntegerField(unique=True, index=True)
    name = CharField(max_length=100)
    last_name = CharField(max_length=150)
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'user'
        order_by = ('-created',)

    def __str__(self):
        return self.name


def create_migrate():
    db.connect()
    db.create_tables([User])
    db.close()


def init_database():
    db.connect()
