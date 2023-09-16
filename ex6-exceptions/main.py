try:
  print(3/0)
except ArithmeticError as error:
  print("ArithmeticError exception occurred,", error.__str__())
finally:
  print("The 'try except' is finished")

class MyException(BaseException):
    pass

try:
    raise MyException('random failure')
except BaseException as error:
    print('Custom error occurred', error.__str__())
