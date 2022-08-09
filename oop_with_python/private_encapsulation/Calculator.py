from unittest import result


class Calculator:

    def calculate(self, op: str, num1: float, num2: float) -> float:
        if op == '+':
            return self.__add(num1, num2)
        elif op == '-':
            return self.__subtract(num1, num2)
        else:
            print('Invalid operation...')

    def __add(self, num1: float, num2: float):
        return num1 + num2

    def __subtract(self, num1: float, num2: float) -> float:
        return num1 - num2


calculator = Calculator()
result = calculator.calculate('+', 3, 2)
result = calculator.calculate('-', 3, 2)

print(result)
