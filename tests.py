import unittest

from figures import Circle, Triangle


class TestFigures(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.get_area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.get_area(), 6.0)

    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 4)

    def test_triangle_is_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())


if __name__ == '__main__':
    unittest.main()
