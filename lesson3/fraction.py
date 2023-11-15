"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""

from math import gcd  # greatest common divisor


class Fraction:
    def __init__(self, numerator, denominator):
        """Конструктор, принимающий числитель и знаменатель дроби"""
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"{Fraction.__name__}({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator,
                            self.denominator)

        else:
            # print("надо искать НОК")
            new_denominator = Fraction.lcm(self.denominator, other.denominator)

            multiplier_self = new_denominator // self.denominator
            multiplier_other = new_denominator // other.denominator

            new_self_numerator = self.numerator * multiplier_self

            new_other_numerator = other.numerator * multiplier_other

            return Fraction(new_self_numerator + new_other_numerator,
                            new_denominator)


fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4

# Fraction(1, 2)
# 1/2
# 5/4
#
# Process finished with exit code 0