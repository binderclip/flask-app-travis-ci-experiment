from my_app.models.person import Person
from my_app.models.pet import Pet
from my_app.init import db


def create_tables():
    db.create_tables([Person, Pet])


def drop_tables():
    db.drop_tables([Person, Pet])
