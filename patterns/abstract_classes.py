from abc import ABC, ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        raise NotImplemented


class Horse(Animal):
    pass


class Cat(Animal):
    def make_sound(self):
        print("meow")


class Dog(Animal):
    def make_sound(self):
        print("woof")
