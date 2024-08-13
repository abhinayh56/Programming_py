from abc import ABC, abstractmethod

# abstract class and methods in python
# python by default does not support abstract classes. it is supported in java, c#
# method with declaration but without definition is called abstract emthod
# class with abstract method is abstract called class
# creating abstract tmod and class in python requires ABC module. Abstract base class module
# we can not create object of abstrat classes

class Computer(): # this is not an abstract class
    def process(self): # this is not a abstract method: only declaration not defition
        # print("running")
        pass

com = Computer() # because object can be created
com.process()

class Computer(ABC): # this is abstract class
    @abstractmethod
    def process(self): # this is abstract method: only declaration not definition
        # print("running")
        pass
    
    @abstractmethod
    def memory(self):
        pass

class Laptop(Computer):
    def process(self):
        print("running")
    
    def memory(self):
        print("1TB HDD")

class Whiteboard(Computer):
    def write(self):
        print("it's writing")

class Programmer:
    def work(self, com):
        print("solve bugs")
        com.process()

# com = Computer()
com1 = Laptop()
com2 = Whiteboard()

com1.process()

prog_1 = Programmer()
prog_1.work(com1)