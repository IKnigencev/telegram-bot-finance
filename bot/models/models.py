from peewee import *


db = SqliteDatabase("my_project.db")


class MixinConfig(Model):
    class Meta:
        database = db


class User(MixinConfig):
    id_telegram = IntegerField(unique=True, index=True)
    name = CharField(max_length=100)
    last_name = CharField(max_length=150)

    def __str__(self):
        return self.name


def init_database():
    db.connect()
    db.close()
