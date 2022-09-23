# Реализуйте методы, позволяющие переводить комплексное число в экспоненциальную форму и обратно.
import math


class CN:
    def alg_exp(self):
        if self.x == 0 and self.y == 0:
            print('Вы вышли из области определения')
            return
        self.x, self.y = math.hypot(self.x, self.y), math.atan2(self.y, self.x)
        return

    def exp_alg(self):
        if self.x < 0:
            print('Вы вышли из области определения')
            return
        self.x, self.y = self.x*math.cos(self.y), self.x*math.sin(self.y)
        return

    def get(self):
        return self.x, self.y

    def set(self, my_x, my_y):
        self.x = my_x
        self.y = my_y
        return

    def __init__(self, my_x=0, my_y=0):
        self.set(my_x, my_y)
        return


a = CN(-1, 0)
a.alg_exp()
print(*a.get())
a.set(1, math.pi/2)
print(*a.get())
a.exp_alg()
print(*a.get())
print('Hi')