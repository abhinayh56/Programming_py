class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"Config is: {self.cpu} , {self.ram}gb, 1TB")

com1 = Computer('i5', 16) # it is object creation
com2 = Computer('Ryzen 3', 8)

com1.config()
Computer.config(com2) # object is passed inside the method of a class Computer (self)

