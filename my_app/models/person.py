from peewee import CharField
from my_app.models.base import BaseModel


class Person(BaseModel):
    name = CharField()
