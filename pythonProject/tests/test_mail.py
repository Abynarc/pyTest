import pytest

@pytest.fixture
def set_up():
    print('Авторизация выполнена')

def test_send_mail_1(set_up):
    print('Письмо отправлено')

def test_send_mail_2(set_up):
    print('Второе письмо отправлено')
