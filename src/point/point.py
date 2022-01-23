from __future__ import annotations
from math import hypot


class Point:
    __slots__ = ('_x', '_y')

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x = float(x)
        self._y = float(y)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: Point) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Point) -> bool:
        return not self == other

    def distance(self, other: Point) -> float:
        if not isinstance(other, self.__class__):
            raise TypeError()
        return hypot(self.x - other.x, self.y - other.y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value: float) -> None:
        self._x = float(value)

    @y.setter
    def y(self, value: float) -> None:
        self._y = float(value)


if __name__ == '__main__':  # pragma: no cover
    point = Point(10, 15)
    point2 = Point()

    print()
