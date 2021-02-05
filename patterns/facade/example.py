class Ram:
    def method_b(self):
        pass


class Cpu:
    def method_a(self):
        pass


class Ssd:
    def method_x(self):
        pass


class Computer:
    def __init__(self):
        self.ram = Ram()
        self.ssd = Ssd()
        self.cpu = Cpu()

    def start(self):
        self.ram.method_b()
        self.cpu.method_a()
        self.ssd.method_x()


c = Computer()
c.start()