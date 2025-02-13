"""
Напишите класс Employee, представляющий сотрудника, имеющий следующие методы:

- __init__(self, name, salary): конструктор, принимающий имя сотрудника
и его зарплату;
- get_salary(self): метод, который возвращает зарплату сотрудника.

Напишите класс Manager, наследующийся от класса Employee, представляющий
менеджера, имеющий следующие методы:

- __init__(self, name, salary, bonus): конструктор, принимающий имя менеджера,
его зарплату и бонус;
- get_salary(self): метод, который возвращает зарплату менеджера плюс его бонус.
"""


class Employee:
    def __init__(self, name, salary):
        """Конструктор, принимающий имя сотрудника и его зарплату"""
        self.name = name
        self.salary = salary


    def get_salary(self):
        """Метод, который возвращает зарплату сотрудника"""
        return self.salary


class Manager:
    def __init__(self, name, salary, bonus):
        """Конструктор, принимающий имя менеджера, его зарплату и бонус"""
        self.name = name
        self.salary = salary
        self.bonus = bonus


    def get_salary(self):
        """Метод, который возвращает зарплату менеджера плюс его бонус"""
        return self.salary + self.bonus


employee = Employee("John", 5000)
print(employee.get_salary())  # 5000

manager = Manager("Jane", 10000, 5000)
print(manager.get_salary())  # 15000

# /usr/bin/python3 /Users/andrejskovorodnikov/Desktop/oop_additional_tasks/
# lesson4/employee.py
# 5000
# 15000
#
# Process finished with exit code 0