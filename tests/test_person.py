from my_app.app import create_person


def test_create_person(person_1):
    person = create_person('Jack')
    assert person.id
    assert person_1.id
