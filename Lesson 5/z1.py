#1) Реализовать структуру наследования классов геометрических фигур. Каждый класс должен обладать
#    методами __.area()__ и __.perimeter()__. Среди обязательных для реализации структур: круг,
#    треугольник, прямоугольник, квадрат, ромб. Для простоты можно конструировать фигуры из точек,
#    передающихся в порядке обхода по часовой стрелке.

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"


def dist(a, b):
    return ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5


class Shape:
    def __init__(self, type="Shape"):
        self._type = type

    def __str__(self):
        return str(self._type)


class Polygon(Shape):
    def __init__(self, type="Polygon"):
        super().__init__(type)
        self._point = []

    def perimetr(self):
        p = 0
        for i in range(len(self._point) - 1):
            p+=dist(self._point[i], self._point[i+1])
        return p + dist(self._point[-1], self._point[0])

    def area(self):
        s = 0
        for i in range(len(self._point) - 2):
            a = dist(self._point[-1], self._point[i])
            b = dist(self._point[i], self._point[i+1])
            c = dist(self._point[i+1], self._point[-1])
            p = (a + b + c) / 2
            s += (p * (p - a) * (p - b) * (p - c))**0.5
        return s


class Triangle(Polygon):
    def __init__(self, p1, p2, p3, type="Triangle"):
        super().__init__(type)
        self._point.append(p1)
        self._point.append(p2)
        self._point.append(p3)

    def __str__(self):
         return " ".join([super().__str__(), self._point[0].__str__(), self._point[1].__str__(),
                   self._point[2].__str__()])


class Parallelogram(Polygon):
    def __init__(self, p1, p2, p3, p4, type="Parallelogram"):
        super().__init__(type)
        self._point.append(p1)
        self._point.append(p2)
        self._point.append(p3)
        self._point.append(p4)

    def __str__(self):
         return " ".join([super().__str__(), self._point[0].__str__(), self._point[1].__str__(),
                   self._point[2].__str__(), self._point[3].__str__()])


class Rhombus(Parallelogram):
    def __init__(self, p1, p2, p3, p4, type="Rhombus"):
        super().__init__(type)


class Rectangle(Parallelogram):
    def __init__(self, p1, p2, p3, p4, type="Rectangle"):
        super().__init__(type)


class Square(Rectangle, Rhombus):
    def __init__(self, p1, p2, p3, p4, type="Square"):
        super().__init__(type)


class Circle(Shape):
    def __init__(self, rad, centre, type = "Circle"):
        super().__init__(type)
        self._rad = rad
        self._centre = centre

    def __str__(self):
         return " ".join([super().__str__(), str(self._rad), self._centre.__str__()])

    def area(self):
        import math
        return math.pi * self._rad**2

    def perimetr(self):
        import math
        return 2 * math.pi * self._rad

a = Circle(5, Point())
print(a)
print(a.perimetr())
print(a.area())
