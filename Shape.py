import math

class Shape:
    def __init__(self, name, side):
        self.name = name
        self.side = side
        self.area = 0
        self.cir = 0

    def setArea(self):
        pass

    def getCircumference(self):
        pass

    def view(self):
        print("Name", self.name, self.area, self.cir)


class Triangle(Shape):
    def __init__(self, len):
        super().__init__("Triangle", 3)
        self.len = len

    def setArea(self):  # Override method
        self.area = 0.5 * self.len * self.len

    def getCircumference(self): #Override method
        self.cir = 3*self.len

class Circle(Shape):
    def __init__(self, r):
        super().__init__("Circle", 0)
        self.r = r

    def setArea(self):  # Override method
        self.area = math.pi * math.pow(self.r,2)

    def getCircumference(self): #Override method
        self.cir = 2 * math.pi * self.r

ob = Triangle(10)
ob.setArea()
ob.getCircumference()
ob.view()

ob2 = Circle(20)
ob2.setArea()
ob2.getCircumference()
ob2.view()