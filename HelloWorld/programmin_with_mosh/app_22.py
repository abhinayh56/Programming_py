class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

# if __name__ == "__main__":
#     com1 = Computer()
#     print(type(com1))

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()

# all four above are ame