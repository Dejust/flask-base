from flask import current_app


def index_page():
    calculator = current_app.calculator
    a, b, factor = 2, 2, calculator.factor
    return '<h1>({} + {}) * {} = {}'.format(a, b, factor, calculator.add(a, b))
