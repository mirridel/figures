import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    # вычисление площади фигуры без знания типа фигуры
    @staticmethod
    def calculate_area(figure):
        return figure.get_area()


class Circle(Figure):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("invalid radius")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        if not (a + b > c and b + c > a and a + c > b) or not (a > 0 and b > 0 and c > 0):
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    # проверка на то, является ли треугольник прямоугольным
    def is_right(self):
        alpha = self.get_degree(self.b, self.c, self.a)
        beta = self.get_degree(self.a, self.c, self.b)
        gamma = self.get_degree(self.a, self.b, self.c)
        return alpha == 90 or beta == 90 or gamma == 90

    def get_degree(self, x1, x2, y):
        expr = (x1 ** 2 + x2 ** 2 - y ** 2) / (2.0 * x1 * x2)
        return math.degrees(math.acos(expr))
