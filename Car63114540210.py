import datetime
class Vehicle:
    scount = 0
    Species = []

    def __init__(self, brand, model, gas_tank_size):
        self.brand = brand
        self.model = model
        self.gas_tank_size = gas_tank_size
        Vehicle.scount += 1

    def showStatus(self):
        if (self.gas_tank_size > 10):
            return "FULL"
        elif (self.gas_tank_size < 2):
            return "QUITE EMPTY"
        elif (self.gas_tank_size == 0):
            return "EMPTY"
        else:
            return "NORMAL"

    @classmethod
    def showscount(cls):
        print(cls.scount, cls.Species)

    @staticmethod
    def dataCar(p,y):
        now = datetime.datetime.now()
        year = now.year-y
        if (year > 10):
            return (p*0.002)*year
        elif (year < 3):
            return (p*0.008)*year
        else:
            return (p*0.005)*year

    def showInfo(self):
        print(self.brand, self.model, self.gas_tank_size)

obj1 = Vehicle("Honda","vios",5)
print(obj1.showStatus())
obj1.showInfo()
print(Vehicle.dataCar(15000,15))