import pytest
from my_app.app import create_person, create_pet


@pytest.fixture(autouse=True)
def db(request):
    from my_app.model_utils.table import create_tables, drop_tables

    # print('create tables...')
    create_tables()

    def fin():
        # print('drop tables...')
        drop_tables()
    request.addfinalizer(fin)


@pytest.fixture()
def person_1():
    return create_person('Andrew')


@pytest.fixture()
def pet_1(person_1):
    return create_pet(person_1.id, 'Timmy')
