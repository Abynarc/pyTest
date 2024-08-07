import pytest


@pytest.fixture
def set_up():
    print('Авторизация выполнена')
    yield
    print('Выход из системы')

@pytest.fixture(scope='module')
def some():
    print('Начало')
    yield
    print('Конец')