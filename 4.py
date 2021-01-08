class Parent():

    def show(self):
        print("Inside Parent")


class Child(Parent):

    def show(self):
        print("Inside Child")


jb = Parent()
jb.show()
bj = Child()
bj.show()
