"""
Напишите класс Timer, который будет вычислять время выполнения блока кода.
Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb):
магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import time


class Timer:

    def __init__(self):
        self.elapsed_time = 0

    def __enter__(self):
        """Магический метод, который запускает таймер"""
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Магический метод, который останавливает
        таймер и выводит время выполнения блока кода."""
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time


with Timer() as timer:
    # блок кода
    print("Something for test")
    for i in range(1000):
        print(i)

print("Execution time:", timer.elapsed_time)

