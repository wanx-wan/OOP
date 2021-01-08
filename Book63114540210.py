class Book:
    Author = ""
    Title = ""

    def __init__(self, price, author, Title, Pubyear):
        self.Title = Title
        self.author = author
        self.Price = price
        self.Author = "	Markas"
        self.Title = "Scooby-Doo"
        self.Pubyear = Pubyear

    def displayData(self):
        print("Price: ", self.Price, "Author: ", self.Author, "Title: ", self.Title, "Pubyear: ", self.Pubyear)
        print(Book)


obj1 = Book(99, "Author:", "Title:", 2007)
obj1.displayData()
