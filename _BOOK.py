class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def showEpisode(self):
        pass

    def getPrice(self):
        self.price = self.price * (7 / 100)

    def showtoString(self):
        print(self.title, self.price)


class Cartoon(Book):
    def __init__(self, episode):
        super().__init__("Cartoon", 1)
        self.episode = ["Doragon Bōru Zetto Gaiden: Saiyajin Zetsumetsu Keikaku\n",
                        "Doragon Bōru Ossu! Kaette Kita Son Gokū to Nakama-tachi!!\n", 
                        "Doragon Bōru: Suupaa Saiyajin Zetsumetsu Keikaku\n" 
                        "Doragon Bōru: Episōdo obu Bādakku"]

    def showEpisode(self):
        for i in range(0, len(self.episode)):
            print(self.episode[i], end='')


obj = Book("Dragonball", 4000)
obj.getPrice()
obj.showtoString()
print()
print("\"Special Episode\"")

obj1 = Cartoon(Book)
obj1.showEpisode()