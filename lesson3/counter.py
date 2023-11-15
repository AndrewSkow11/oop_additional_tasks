"""
Напишите класс Counter, имеющий следующие методы:

- __init__(self): конструктор, создающий счетчик и устанавливающий его значение в 0;
- __call__(self): магический метод, который позволяет использовать объект класса Counter как функцию, возвращающую текущее значение счетчика;
- increment(self): метод, увеличивающий значение счетчика на 1.
"""


class Counter:

    def __init__(self):
        """конструктор, создающий счетчик и устанавливающий его значение в 0;"""
        self.counter = 0

    def __call__(self):
        return self.counter

    def increment(self):
        self.counter += 1


counter = Counter()
print(counter())  # 0

counter.increment()
print(counter())  # 1

counter.increment()
print(counter())  # 2


# /usr/bin/python3 /Users/andrejskovorodnikov/Desktop/oop_additional_tasks/lesson3/counter.py
# 0
# 1
# 2
#
# Process finished with exit code 0