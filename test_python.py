import math
numbers = [0, 1, 2, 3, 4, 5]


def test_filter():
    assert list(filter(lambda x: x % 2 == 0, numbers)) == [2,4]


def test_map():
    assert list(map(lambda x: x + 1, number)) == [1, 2, 3, 4, 5, 6]


def test_sorted():
    assert list(sorted(numbers, reverse = True)) == [5, 4, 3, 2, 1, 0]


def test_pi():
    assert round(math.pi, 5) == 3.14159


def test_sqrt():
    assert math.sqrt(25) == 5


def test_pow():
    assert math.pow(5,2) == 25


def test_hypot():
    assert math.hypot(3, 4) == 5

