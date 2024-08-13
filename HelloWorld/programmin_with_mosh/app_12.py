# classes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")
    
    def get_coordinates(self):
        return self.x, self.y
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

p1 = Point(2,4)
print(p1.get_coordinates(), type(p1.get_coordinates()))
print(p1.x)

p1.val = "aabcdef"
print(p1.val)

