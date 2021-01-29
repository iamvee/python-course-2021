class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        ratio = (value / self.area) ** 0.5
        self.side = self.side * ratio


if __name__ == '__main__':
    s = Square(6)
    print(s.side, s.area)

    s.side = 10
    print(s.side, s.area)

    s.area = 144
    print(s.side, s.area)
