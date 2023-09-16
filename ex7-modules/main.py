import my_calc.calculator, my_calc.scientific_calculator

calc = my_calc.calculator.Calculator()

print(1, "+", 2, "=", calc.add(1, 2))

sci_calc = my_calc.scientific_calculator.ScientificCalculator()

print(2, "^2=", sci_calc.square(2))
print(1, "+", 2, "=", sci_calc.add(1, 2))
