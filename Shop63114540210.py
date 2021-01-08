class Shop:
    payment = "ThailandPost"

    def __init__(self, product, stores, quantity, price, payment):
        if product == "vegetable":
            self.product = "Lettuce"
            self.stores = "UBU vegetable shops."
            if quantity > 5:
                self.quantity = "You get a 50% discount."
                self.price = "Currently, you have to pay 50% of the full price."
            else:
                self.quantity = "Please purchase additional items to receive a 50% discount."
                self.price = "Currently, you have to pay 50% of the full price."
                if payment == "InternetBanking":
                    self.payment = payment
                elif payment == "Cash on delivery":
                    self.payment = "Flash express"
                else:
                    self.payment = "This type of payment is not supported."

        elif product == "fruit":
            self.product = "Mango"
            self.stores = "UBU fruit shops."
            if quantity > 5:
                self.quantity = "You get a 50% discount."
                self.price = "Currently, you have to pay 50% of the full price."
            else:
                self.quantity = "Please purchase additional items to receive a 50% discount."
                self.price = "Currently, you have to pay 50% of the full price."
                if payment == "InternetBanking":
                    self.payment = payment
                elif payment == "Cash on delivery":
                    self.payment = "Flash express"
                else:
                    self.payment = "This type of payment is not supported."

        elif product == "2 things":
            self.product = "You choose both types."
            self.stores = "UBU vegetable and fruit shops."
            if quantity > 5:
                self.quantity = "You get a 50% discount."
                self.price = "Currently, you have to pay 50% of the full price."
            else:
                self.quantity = "Please purchase additional items to receive a 50% discount."
                self.price = "Currently, you have to pay 50% of the full price."
                if payment == "InternetBanking":
                    self.payment = payment
                elif payment == "Cash on delivery":
                    self.payment = "Flash express"
                else:
                    self.payment = "This type of payment is not supported."

        else:
            self.product = "The product you are currently selecting does not exist. If you want the product, " \
                           "please make a new one. "
            self.stores = "There are no participating stores."
            self.quantity = "You will receive a 50% discount if the specified quantity is reached."
            self.price = "You have not selected the item."
            self.payment = "Please make a new product list."
            
    def displayData(self):
        print("Thank you for purchasing products through Shop application. ", "Product of your choice:", self.product,
              "Stores:", self.stores, "Quantity:", self.quantity, "You have to pay:", self.price,
              "Delivery", self.payment)
        print(Shop)


obj1 = Shop("fruit", "vegetable shops", 2,"price","Cash on delivery")
obj1.displayData()