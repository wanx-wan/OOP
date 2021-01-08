class TmpEmployee :
    def __init__(self, Hour):
        self.Hour = Hour

    def ManHour (self):
        self.MHour = self.Hour*200

    def Show (self):
        print(self.MHour)


class employee_Fund (TmpEmployee):
    def __init__(self, MHour):
        super().__init__(11)
        self.MHour = MHour
    
    def Foundd(self):
        self.salary = self.MHour*(3 / 100)

    def showsh (self):
        print(self.salary)

aa = TmpEmployee(2)
aa.ManHour()
aa.Show()

aa = employee_Fund(400)
aa.Foundd()
aa.showsh()