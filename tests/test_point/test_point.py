import pytest
from point.point import Point


def test_default_constructor():
    p = Point()

    assert p.x == 0.0
    assert p.y == 0.0


def test_constructor():
    p = Point(4, 6)

    assert p.x == 4.0
    assert p.y == 6.0


def test_string_repr():
    assert str(Point()) == '(0.0, 0.0)'


def test_setters():
    p = Point()

    assert p.x == 0.0
    assert p.y == 0.0

    p.x = 42
    p.y = 24

    assert p.x == 42.0
    assert p.y == 24.0


def test_operators():
    p1, p2 = Point(), Point()
    p3 = Point(2, 4)

    assert p1 == p2
    assert p1 != p3
    assert not p1 != p2
    assert not p3 == p1


def test_distance():
    p1, p2 = Point(10, 15), Point()

    assert p1.distance(p2) == 18.027756377319946


def test_distance_exception():
    with pytest.raises(TypeError):
        assert Point().distance('abcde') == 18.027756377319946
