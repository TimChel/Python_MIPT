# Добавьте функции, позволяющие складывать, вычитать, умножать и делить два комплексных числа, результатом работы
# которых будет новое комплексное число.
class CN:
    def get(self):
        return self.x, self.y

    def set(self, my_x, my_y):
        self.x = my_x
        self.y = my_y
        return

    def __init__(self, my_x=0, my_y=0):
        self.set(my_x, my_y)
        return


def sloj(a, b):
    return a.get()[0] + b.get()[0], a.get()[1] + b.get()[1]


def vich(a, b):
    return a.get()[0] - b.get()[0], a.get()[1] - b.get()[1]


def umn(a, b):
    return a.get()[0]*b.get()[0] - a.get()[1]*b.get()[1], a.get()[0]*b.get()[1] + a.get()[1]*b.get()[0]


def sopr(a):
    return CN(a.get()[0], -1*a.get()[1])


def delen(a, b):
    return umn(a, sopr(b))[0]/(b.get()[0]**2 - b.get()[1]**2), umn(a, sopr(b))[1]/(b.get()[0]**2 + b.get()[1]**2)

a = CN(4, 5)
b = CN(1, 2)
print('Сложение:', sloj(a, b))
print('Вычитание:', vich(a, b))
print('Умножение:', umn(a, b))
print('Деление:', delen(a, b))