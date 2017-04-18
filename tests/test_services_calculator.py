from tests.base import IntegrationTestCase


class CalculatorServiceTestCase(IntegrationTestCase):
    def test_add(self):
        calculator = self.test_app.calculator
        expected_result = (2 + 2) * calculator.factor
        self.assertEqual(expected_result, calculator.add(2, 2))
