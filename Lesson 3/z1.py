# Создайте класс для хранения комплексных чисел с инициализатором.
class CN:
    def __init__(self, my_x=0, my_y=0):
        self.x = my_x
        self.y = my_y
        return


a = CN(1, 2)
print(a.x, a.y)
print('Hi')
