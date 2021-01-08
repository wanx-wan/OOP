class Employee:
    def __init__(self, eid, ename):
        self.eid = eid
        self.ename = ename

    def calSalary(self):
        pass

    def calFund(self):
        pass

    def money(self):
        pass

    def working(self):
        pass

    def toString(self):
        print(self.eid, self.ename)

class TmpEmployee(Employee):
    def __init__(self, manhour):
        super().__init__("ID", "Name")
        self.working_hour = 1
        self.manhour = manhour
        self.salary = 200
        self.Funds = 0
        self.tax = 3

    def calFund(self):
        self.Fund = 1 * self.tax
        print(self.Fund)

    def money(self):
        self.manhour = self.salary * self.manhour

    def working(self):
        self.working_hour = self.manhour/self.salary
        print(self.working_hour)

    def toString(self):
        print(self.manhour)
    
print("ID and Name")
obj = Employee("112234", "Wanchana")
obj.toString()

print("Employee Fund")
obj2 = TmpEmployee(20)
obj2.calFund()
print("Working hours")
obj2.money()
obj2.working()
print("Amount received")
obj2.toString()