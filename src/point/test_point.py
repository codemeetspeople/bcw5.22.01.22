import unittest
from point import Point


class TestPoint(unittest.TestCase):
    def test_constrtuctor(self):
        p = Point()
        self.assertEqual(p.x, 0.0)
        self.assertEqual(p.y, 0.0)

        p = Point(2, 19)
        self.assertEqual(p.x, 2.0)
        self.assertEqual(p.y, 19.0)

        with self.assertRaises(TypeError):
            Point(Point(), 0.0)

        with self.assertRaises(ValueError):
            Point('abc', 0.0)

    def test_operators(self):
        p1, p2 = Point(), Point()
        p3 = Point(1, 7)

        self.assertTrue(p1 == p2)
        self.assertFalse(p1 != p2)
        self.assertTrue(p1 != p3)
        self.assertFalse(p1 == p3)


if __name__ == '__main__':
    unittest.main()
