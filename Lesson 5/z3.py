#3) Написать программу калькулятор, которая считывает два комплексных числа и проводит с ними
#    арифметические операции с обработкой вылезающих исключений: например если в процессе деления
#    возникнет ZeroDivisionError, программа должна продолжить работу, предложив пользователю
#    выбрать другую операцию.
import numbers
import math


class ExponentialOverlapError(Exception):
    pass


class ComplexNumbers:
    def get(self):
        return self._x, self._y

    def set(self, my_x, my_y):
        if isinstance(my_x, numbers.Number) and isinstance(my_y, numbers.Number):
            self._x = my_x
            self._y = my_y
        else:
            raise ValueError

    def __init__(self, my_x=0, my_y=0):
        self.set(my_x, my_y)

    def __str__(self):
        if self._y > 0:
            return str(self._x)+' + i*'+str(self._y)
        if self._y < 0:
            return str(self._x)+' - i*'+str(-1*self._y)
        return str(self._x)

    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            return self._x == other and self._y == 0
        if isinstance(other, ComplexNumbers):
            return self._x == other._x and self._y == other._y

    def __ne__(self, other):
        if self == other:
            return False
        return True

    def __getitem__(self, key):
        if key == 0:
            return self._x
        if key == 1:
            return self._y

    def __setitem__(self, key, value):
        if key == 0:
            self._x = value
            return
        if key == 1:
            self._y = value
            return

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return ComplexNumbers(self._x + other, self._y)
        if isinstance(other, ComplexNumbers):
            return ComplexNumbers(self._x + other._x, self._y + other._y)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            return ComplexNumbers(self._x - other, self._y)
        if isinstance(other, ComplexNumbers):
            return ComplexNumbers(self._x - other._x, self._y - other._y)

    def __rsub__(self, other):
        return -1 * self + other

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return ComplexNumbers(self._x * other, self._y * other)
        if isinstance(other, ComplexNumbers):
            return ComplexNumbers(self._x * other._x - self._y * other._y, self._y * other._x + self._x * other._y)

    def __rmul__(self, other):
        return self * other

    def sopr(self):
        return ComplexNumbers(self._x, -1 * self._y)

    def __abs__(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return ComplexNumbers(self._x / other, self._y / other)
        if isinstance(other, ComplexNumbers):
            return ComplexNumbers((self * other.sopr())._x / abs(other), (self * other.sopr())._y / abs(other))

    def __rtruediv__(self, other):
        return ComplexNumbers(other, 0) / self

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def __itruediv__(self, other):
        return self / other

    def exp(self):
        if self._x == 0 and self._y == 0:
            raise ExponentialOverlapError()
        self._rad, self._angle = math.hypot(self._x, self._y), math.atan2(self._y, self._x)
        return str(self._rad)+' * e^(i*'+str(self._angle)+')'


print('Здравствуйте, Вас приветствует Мистер Калькулятор Вселенной 2022! \nЯ слышал, что Вам нужна помощь '
      'с операциями над полем комплексных чисел.')
while True:
    print('Для выбора операции введите один из следующих знаков: "+", "-", "*", "/"')
    operation = input()
    if operation in '+-*/':
        print('Замечательно!')
        break
    else:
        print('Кажется, что-то пошло не так. Попробуй еще раз!')
while True:
    print('Теперь введи 2 комплексных числа а+ib и c+id в виде: a b c d')
    try:
        compl = list(map(float, input().split()))
        A = ComplexNumbers(compl[0], compl[1])
        B = ComplexNumbers(compl[2], compl[3])
    except ValueError:
        print('Кажется, что-то пошло не так. Попробуй еще раз!')
    else:
        if B == 0 and operation == '/':
            print('Ты что, совсем с ума сошел?! Ты чего на 0 делить вздумал! \n'
                  'А ну быстро ввел новые числа, и чтобы в этот раз без попыток сломать вселенную.')
        else:
            print('Замечательно!')
            break
if operation == '+':
    otvet = A + B
elif operation == '-':
    otvet = A - B
elif operation == '*':
    otvet = A * B
elif operation == '/':
    otvet = A / B
else:
    print('Так, стоп. Ты как сюда попал? Это неправильно, тебя не должно быть здесь. Ты не должен этого видеть! Нееет....')
print('Ответ на вашу задачу находится после знака "=". Рад был помочь. Удачного вам дня!\n',
      '(', A, ')', operation, '(', B, ')', '=', otvet)
