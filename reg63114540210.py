class Reg:
    subject = "There are no courses that can be taken."

    def __init__(self, number, subject, code):
        self.number = number
        self.code = code
        if number == "63123456789":
            self.number = "Please enter these courses."
            if code == "123456":
                self.subject = "English"
            elif code == "987654":
                self.subject = "Thai"
            else:
                self.subject = subject

        elif number == "63987654321":
            self.number = "Please enter these courses."
            if code == "222222":
                self.subject = "Social"
            elif code == "333333":
                self.subject = "Human"
            else:
                self.subject = subject

        else:
            self.branch = "Your student ID number is incorrect."
            self.subject = "Something went wrong"

    def displayData(self):
        print("Check correctness.", 'Student code:', self.number,
              "Your choice:", self.subject,
              "Code:", self.code)
        print(Reg)


obj1 = Reg("63123456789", "Thai", "987654")
obj1.displayData()
