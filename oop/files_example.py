class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    @property
    def precestors(self):
        if self.parent.value == 0:
            return [0]
        return [self.parent.value] + self.parent.precestors