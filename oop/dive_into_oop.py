class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


lst = [1, 2, 3, 4]
out = lst

#
# class NewInt(int):
#     def __add__(self, other):
#         return self * other
#
#
# a = NewInt(7)
# b = NewInt(5)
#
# print(a+b)
