class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")

try:
    number1 = int(number1)
    number2 = int(number2)
    if number2 == 0:
        raise OwnError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(number1 / number2)