

class Animal:
    def make_sound(self):
        raise NotImplemented


class Horse(Animal):
    def make_sound(self):
        print("pitiko pitiko")


class Cat(Animal):
    def make_sound(self):
        print("meow")


class Dog(Animal):
    def make_sound(self):
        print("woof")


def get_animal(name):
    if name in ["cat", "Cat", "gorbe", "koshka"]:
        return Cat()
    elif name in ["sag", "Dog", "dog", "sobaka", "kalb"]:
        return Dog
    elif name in ["asb", "horse"]:
        return Horse


get_animal("gorbe").make_sound()