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

    def viewInfo(self):
        print(self.name, self.area, self.cir)

class Triangle(Shape):
    def __init__(self, len):
        super().__init__("Triangle", 3)
        self.len = len
    
    def setArea(self): #Override method
        self.area = 0.5*self.len*self.len
    
    def getCircumference(self):
        self.cir = 3*self.len

class Circle(Shape):
    def __init__(self, r):
        super().__init__("Circle", 0)
        self.r = r
    
    def setArea(self):
        self.area = math.pi*math.pow(self.r,2)

    def getCircumference(self):
        self.cir = 2*math.pi*self.r
    

obj2 = Triangle(20)
obj3 = Circle(7)
obj2.setArea()
obj3.setArea()
obj2.getCircumference()
obj3.getCircumference()
obj2.viewInfo()
obj3.viewInfo()