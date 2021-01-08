class Parent:
    def __init__(self, x, z):
        self.x = x
        self.z = z
    
    def viewInfo(self):
        print("Parent", self.x, self.z, self.y )

class Child(Parent):
    def __init__(self, x, z,  y):
        Parent.__init__(self, x, z)
        #super().__init__(x, z) #inherit and consructor
        self.y = y

obj1 = Child("I", "luv", "U")
obj1.viewInfo()
