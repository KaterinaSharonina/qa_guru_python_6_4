import math
import random


def test_greeting():
    name = "Анна"
    age = 25
    # Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)


def test_rectangle():
    a = 10
    b = 20
    # Сосчитайте периметр
    perimeter = (a + b) * 2
    assert perimeter == 60
    print(perimeter)
    # Сосчитайте площадь
    area = a * b
    assert area == 200
    print(area)


def test_circle():
    r = 23
    # Сосчитайте площадь
    area = math.pi * (r ** 2)
    assert area == 1661.9025137490005
    print(area)
    # Сосчитайте длину окружности
    length = 2 * math.pi * r
    assert length == 144.51326206513048
    print(length)


def test_random_list():
    # Cоздайте список
    l = random.sample(range(1, 101), 10)
    l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]
    print(l)


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # Удалите повторяющиеся элементы
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l)


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # Создайте словарь
    d = dict(zip(first, second))
    assert isinstance(d, dict)
    assert len(d) == 5
    print(d.values())
