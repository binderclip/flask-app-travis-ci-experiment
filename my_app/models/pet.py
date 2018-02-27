from peewee import CharField, IntegerField
from my_app.models.base import BaseModel


class Pet(BaseModel):
    owner_id = IntegerField()
    name = CharField()
