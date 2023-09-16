class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


calc = Calculator()

print(1, "+", 2, "=", calc.add(1, 2))


class ScientificCalculator(Calculator):
    def square(self, a):
        return a * a


sci_calc = ScientificCalculator()

print(2, "^2=", sci_calc.square(2))
print(1, "+", 2, "=", sci_calc.add(1, 2))
