class People:
    all_people = []

    def __init__(self, name):
        self.name = name
        self.all_people.append(self)

    @classmethod
    def get_population(cls):
        return len(cls.all_people)


for i in range(10):
    p = People(f"person {i}")
    print(p, p.get_population(), People.get_population())
