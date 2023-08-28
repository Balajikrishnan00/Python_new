# operator Overloading
# method Overloading
# constructor Overloading
from abc import abstractmethod


# method Overriding
# constructor Overriding


class Bike:
    def fill(self):
        print("Petrol")


class Truck:
    def fill(self):
        print("Diesel")


class EV:
    def fill(self):
        print("Charging...")


class Vehicles:
    def fill(self):
        print("Get Ready for Ride")


listOfVehicles = [Bike(), Truck(), EV(), Vehicles()]


def fuel(i):
    i.fill()


for i in listOfVehicles:
    fuel(i)


# Operator Overloading

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, another):
        return self.pages + another.pages


b1 = Book(100)
b2 = Book(200)
b3 = Book(300)


# print(b1 + b2)


class Mobile:
    def __init__(self, brand, model, price, offer):
        self.brand = brand
        self.model = model
        self.price = price
        self.offer = offer

    def __add__(self, other):
        return self.__showOffer__() + other.__ccOffer__(obj)

    def __showOffer__(self):
        return self.price * (self.offer / 100)


class CreditCard:
    def __init__(self, bankName, cardType, ccOffer):
        self.bankName = bankName
        self.cardType = cardType
        self.ccOffer = ccOffer

    def __ccOffer__(self, another):
        return another.price * (self.ccOffer / 100)


m1 = Mobile("Samsung", "Samsung Galaxy Ultra S2 Pro", 145000, 3)
obj = m1
cc1 = CreditCard("Axis Bank", "Platinum", 3)
# print(m1.__showOffer__())
# print(cc1.__ccOffers__(m1))
print(m1 + cc1)


class Test:
    def calculate(self, *n):
        return sum(n)


t1 = Test()
print(t1.calculate(10, 12, 30))


class Parent:
    def study(self):
        print("study doctor")


class Child(Parent):
    def study(self):
        print("Study computer science")
        super().study()


c1 = Child()
c1.study()

