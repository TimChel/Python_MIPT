#Доработайте класс комплексного числа из прошлого занятия: переопределите математические
#операторы (+, -, /, *, ==), так, чтобы она работали с другими комплексными и со стандартными
#числами. Добейтесь правильной работы с комплексным числом функций print(), abs(), а также
#реализуйте обращение к действительной и мнимой части комплексного числа через x[0] и x[1]
#соответственно (как для получения так и для присваивания).
import numbers
import math


class ComplexNumbers:
    def get(self):
        return self._x, self._y

    def set(self, my_x, my_y):
        self._x = my_x
        self._y = my_y

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

A = ComplexNumbers(34, 54)
B = ComplexNumbers(34, 54)
C = ComplexNumbers(34, 0)
p = 34
print(p == C)