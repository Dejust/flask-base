"""
Пример разработки собственного сервиса для Flask
"""


class Calculator:

    def __init__(self, factor):
        self.factor = factor

    def add(self, a, b):
        return (a + b) * self.factor
