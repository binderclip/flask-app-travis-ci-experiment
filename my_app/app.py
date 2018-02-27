from my_app.models.person import Person
from my_app.models.pet import Pet


def create_person(name):
    return Person.create(name=name)


def create_pet(person_id, name):
    return Pet.create(owner_id=person_id, name=name)


def person_s_pets(person_id):
    return list(Pet.select().where(Pet.owner_id == person_id).order_by(Pet.id))
