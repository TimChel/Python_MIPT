# Обеспечьте его необходимыми геттерами и сеттерами.
class CN:
    def get(self):
        return self.x, self.y

    def set(self, my_x, my_y):
        self.x = my_x
        self.y = my_y
        return

    def __init__(self, my_x, my_y):
        self.set(my_x, my_y)
        return


a = CN(1, 2)
print(a.x, a.y)
print('Hi')