import math


class Parallelogram:
    def __init__(self, width, height, angle):
        self.width = width
        self.height = height
        self.angle = angle

    @property
    def area(self):
        return self.width * self.height * math.sin(math.radians(self.angle))

    @area.setter
    def area(self, value):
        ratio = (value / self.area) ** 0.5
        self.width = self.width * ratio
        self.height = self.height * ratio


class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, height, 90)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


s = Square(10)
print(s.area)
s.area = 9
print(s.width)


print(isinstance(s, Square))
print(isinstance(s, Rectangle))
print(isinstance(s, Parallelogram))
print(isinstance(s, object))
print()
print(type(s) == Square)
print(type(s) == Rectangle)
print(type(s) == Parallelogram)