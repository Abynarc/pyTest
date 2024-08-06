import pytest

@pytest.fixture
def set_up():
    print('Авторизация выполнена')

def test_send_mail_1():
    print('Письмо отправлено')

def test_send_mail_2():
    print('Второе письмо отправлено')
