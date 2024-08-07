import pytest


@pytest.mark.run(order=2)
def test_method_1():
    print('Выполнен метод 1')

@pytest.mark.run(order=3)
def test_method_2():
    print('Выполнен метод 2')

@pytest.mark.run(order=1)
def test_method_3():
    print('Выполнен метод 3')

@pytest.mark.run(order=6)
def test_method_4():
    print('Выполнен метод 4')

@pytest.mark.run(order=5)
def test_method_5():
    print('Выполнен метод 5')

@pytest.mark.run(order=4)
def test_method_6():
    print('Выполнен метод 6')