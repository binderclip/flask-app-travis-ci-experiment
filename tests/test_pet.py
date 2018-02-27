from my_app.app import create_pet, person_s_pets


def test_create_person(person_1):
    pet = create_pet(person_1.id, 'Timmy')
    assert pet.id
    assert pet.name == 'Timmy'
    assert pet.owner_id == person_1.id


def test_person_s_pets(person_1, pet_1):
    pets = person_s_pets(person_1.id)
    assert len(pets) == 1
    assert pets[0].owner_id == person_1.id
    create_pet(person_1.id, 'Kimmy')
    pets = person_s_pets(person_1.id)
    assert len(pets) == 2
    assert pets[1].owner_id == person_1.id
