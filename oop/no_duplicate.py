
class NoDuplicate:
    instances = {}

    def __new__(cls, *args, **kwargs):
        val = cls.instances.get(args[0])
        if val is None:
            cls.instances[args[0]] = super().__new__(cls)

        return cls.instances.get(args[0])

    def __init__(self, val):
        self.val = val
        self.instances[self.val] = self


a1 = NoDuplicate("abc")
print(id(a1), a1.instances)

a2 = NoDuplicate("efg")
print(id(a2), a1.instances)

a3 = NoDuplicate("abc")
print(id(a3), a1.instances)


print(a1 is a3)
