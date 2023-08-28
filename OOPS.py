class Supermarket:
    """
        this is supermarket
        """
    manufacturer = "muthu supermarket"
    rice = "Rice Mill"

    def __init__(self, name, price, discount, quanty):
        self.discount = discount
        self.name = name
        self.price = price
        self.quanty = quanty

        print(self.manufacturer)
        print(self.rice)

    def finalPrice(self):
        discount = self.price * (self.discount / 100)
        return self.price - discount

    def invoice(self):
        print("--------------------------------")
        print("\tABC SuperMarker\t")
        print(f"Brand\tPrice\tDiscount\tQuantity\tFinal Price")
        print(f"{self.name}\t{self.price}\t\t{self.discount}\t\t\t\t{self.quanty}\t\t\t{self.finalPrice()}")
        self.rice = " "
        print(self.manufacturer)
        print(self.rice)
        self.rice = " "


bread = Supermarket("ABC", 25, 1.5, 10)
biscuit = Supermarket("ARS", 50, 2, 20)
rice = Supermarket("Balaji", 950, 3, 8)
rice.manufacturer="balaji ricemill"
shampoo = Supermarket("clinicPlus", 2, 2, 5)
iphoneMax14 = Supermarket("Apple", 100000, 19.19, 1)

print(bread.__dict__)
print(biscuit.__dict__)
print(rice.__dict__)
print(iphoneMax14.__dict__)
# print(bread.__dict__)
bread.invoice()
iphoneMax14.invoice()
print(rice.manufacturer)

"""
{'discount': 10, 'name': 'ABC', 'price': 25, 'quanty': 10}
{'discount': 0, 'name': 'ARS', 'price': 50, 'quanty': 20}
{'discount': 0, 'name': 'Balaji', 'price': 950, 'quanty': 8}
{'discount': 3, 'name': 'Apple', 'price': 100000, 'quanty': 1}
"""
