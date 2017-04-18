"""
Демонстрация создания своих страниц в flask app
"""

from flask import current_app


def index_page():
    """
    Тестовая страница
    """
    calculator = current_app.calculator
    first, second, factor = 2, 2, calculator.factor
    return '<h1>({} + {}) * {} = {}'.format(first, second, factor, calculator.add(first, second))
