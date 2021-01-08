class Dog:
    count = 0
    species = []
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        Dog.count += 1

    @classmethod
    def showcount(cls):
        print(cls.count,cls.species)

    @staticmethod
    def dataDog(h):
        if h > 80:
            return "Big Dog"
        elif h < 50:
            return "Small Dog"
        else:
            return "Srandard Dog"
    
    def showInfo(self):
        print(self.name, self.age, self.breed)

    def addspecies(self, speak):
        self.species.append(speak)

obj1 = Dog("Doll", 5, "Chiwawa")
obj1.addspecies("Hello world")
print(Dog.dataDog(40))
obj1.showInfo()