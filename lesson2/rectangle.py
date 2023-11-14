"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
если это квадрат, и False в противном случае
"""


class Rectangle:
    def __init__(self, width, height):
        """конструктор, принимающий ширину и высоту прямоугольника"""
        self.width = width
        self.height = height

    def area(self):
        """метод, возвращающий площадь прямоугольника"""
        return self.width * self.height

    def perimeter(self):
        """Метод, возвращающий периметр прямоугольника"""
        return 2 * (self.width + self.height)

    @classmethod
    def from_diagonal(cls, diagonal, aspect_ratio):
        """принимает диагональ прямоугольника и соотношение
        сторон и возвращающий объект класс Rectangle"""

        a = (diagonal ** 2 / (aspect_ratio ** 2 + 1)) ** (1 / 2)
        b = a * aspect_ratio

        return cls(a, b)

        # Использование теоремы Пифагора: поскольку диагональ является гипотенузой
        # прямоугольного треугольника, можно применить теорему Пифагора для
        # нахождения длины сторон. Если длина диагонали равна D, а стороны
        # прямоугольника – a и b, то теорема Пифагора выглядит
        # следующим образом: D ^ 2 = a ^ 2 + b ^ 2.

        # a == b * aspect ratio
        # (b * aspect ratio) * (b * aspect ratio) + b * b = d * d
        # b ^ 2 * aspect_ratio ^ 2 + b ^ 2  = d ^ 2
        # b ^ 2 * (aspect_ratio ^ 2 + 1) = d ^ 2

    @staticmethod
    def is_square(width, height):
        """Cтатический метод, принимающий ширину и высоту прямоугольника и
        возвращающий True, если это квадрат, и False в противном случае"""

        if width == height:
            return True
        else:
            return False


rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5, 2)
print(rectangle2.area())  # 10.0128
print(rectangle2.perimeter())  # 13.42

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
