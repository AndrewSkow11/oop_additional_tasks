"""
Напишите класс Animal, представляющий животное, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя животного;
- speak(self): метод, который выводит звук, издаваемый животным.

Напишите класс Dog, наследующийся от класса Animal, представляющий собаку,
имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый собакой.

Напишите класс Cat, наследующийся от класса Animal, представляющий кошку,
имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый кошкой.
"""


class Animal:
    def __init__(self, name):
        """Конструктор, принимающий имя животного"""
        self.name = name

    def speak(self):
        """Метод, который выводит звук, издаваемый животным"""
        print("Абстрактный звук абстрактного животного")


class Dog(Animal):
    def speak(self):
        print("Ну вот прям гав!")


class Cat(Animal):
    def speak(self):
        print("Мяу, например")


animal = Animal("Animal")
animal.speak()  # ?

dog = Dog("Dog")
dog.speak()  # Woof!

cat = Cat("Cat")
cat.speak()  # Meow!

# Абстрактный звук абстрактного животного
# Ну вот прям гав!
# Мяу, например
#
# Process finished with exit code 0
