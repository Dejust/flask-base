"""
Пример разработки собственного сервиса для Flask
"""


class Calculator:
    """
    Тестовый сервис для сложения двух чисел
    """

    def __init__(self, factor):
        self.factor = factor

    def add(self, first, second):
        """
        Складывает два числа и умножает на self.factor
        :param second:
        :param first:
        """
        return (first + second) * self.factor

    def sub(self, first, second):
        """
        Вычитает одно из другого и умножает на self.factor
        :param first:
        :param second:
        """
        return (first - second) * self.factor
