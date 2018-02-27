from peewee import Model
from my_app.init import db


class BaseModel(Model):

    class Meta:
        database = db
