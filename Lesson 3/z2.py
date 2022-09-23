# Обеспечьте его необходимыми геттерами и сеттерами.
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


a = CN(1, 2)
print(*a.get())
a.set(25, 30)
print(*a.get())
print('Hi')