

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return Vector(x_new, y_new)

    def __repr__(self):
        return f"VECTOR [{self.x}, {self.y}]"


v1 = Vector(10, 100)
v2 = Vector(1000, 10000)

# v1.x = 10
# v1.y = 100
# v2.x = 1000
# v2.y = 10000

print(v1.x, v1.y, v1.calc_length())
print(v2.x, v2.y, v2.calc_length())

v3 = v1 + v2
print(v3.x, v3.y, v3.calc_length())

print(v1)
print(v2)
print(v3)


