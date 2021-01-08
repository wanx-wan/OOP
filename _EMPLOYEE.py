class Employee:
    def __init__(self, eid, ename):
        self.eid = eid
        self.ename = ename

    def calSalary(self):
        pass

    def calFund(self):
        pass

    def toString(self):
        print(self.eid, self.ename)

class Permanent_emp(Employee):
    def __init__(self, month_salary):
        super().__init__("ID", "Name")
        self.month_salary = month_salary
        self.tax = 3
        self.social_insurance = 5
        self.Fund = 0

    def calFund(self):
        self.Fund = 2*self.tax
        print(self.Fund)

    def caltax(self):
        self.tax = (self.tax/100)*self.month_salary

    def calsocial(self):
        self.social_insurance = (self.social_insurance/100)*self.month_salary

    def calSalary(self):
        self.month_salary = (self.month_salary - self.tax ) - self.social_insurance

    def toString(self):
        print(self.month_salary)

print("ID and Name employee")
obj = Employee("112233", "Wanchai")
obj.toString()

print("Calculate Employee Fund")
obj1 = Permanent_emp(15000)
obj1.calFund()
print("Calculate Salary Balance")
obj1.caltax()
obj1.calsocial()
obj1.calSalary()
obj1.toString()