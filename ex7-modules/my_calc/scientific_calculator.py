from . import calculator


class ScientificCalculator(calculator.Calculator):
    def square(self, a):
        return a * a
