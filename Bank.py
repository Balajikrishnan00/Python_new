class Bank:
    BankName = "State Bank of India,"" SBI"

    def __init__(self, customerName, accountNumber, ):
        self.aadharNumber = None
        self.panNumber = None
        self.customerName = customerName
        self.accountNumber = accountNumber

    def accountOpen(self, ):
        pass

    def accountClose(self):
        pass

    def deposit(self, customerName, accountNumber, amount):
        pass

    def updateAadharNumber(self, aadharNumber):
        if aadharNumber.isdigit() and len(aadharNumber) == 12:
            self.aadharNumber = aadharNumber

    def updatePanNumber(self, panNumber):
        if len(panNumber) == 10:
            self.panNumber = panNumber

    def showCustomerDetails(self):
        return self.__dict__

    @classmethod
    def classMethod(cls):
        print("Class Method")

    @staticmethod
    def staticMethod():
        print("Static Method")


c1 = Bank("Balaji", 123)
c1.classMethod()
c1.staticMethod()
Bank.classMethod()
Bank.staticMethod()


class VasanthAndCoHeadOffice:
    branch = "HeadOffice"

    def __init__(self):
        self.H_offer = 1000


class VasanthAndCoMadurai(VasanthAndCoHeadOffice):
    branch = "Madurai"

    def __init__(self):
        super().__init__()
        self.BranchOffer = 500


customer1 = VasanthAndCoMadurai()

customer2 = VasanthAndCoHeadOffice()
print(customer1.H_offer)


class HumanBeing:

    def __init__(self, name, age, ):
        self.name = name
        self.age = age

    def humanDetails(self):
        print(self.name)
        print(self.age)


class Employee(HumanBeing):

    def __init__(self, name, age, empID, empSalary):
        super().__init__(age, name)
        self.empID = empID
        self.empSalary = empSalary

    def empDetails(self):
        print(self.name)
        print(self.age)
        print(self.empID)
        print(self.empSalary)

    def __str__(self):
        return "HI"


obj1 = Employee("Balaji", 26, 123, 10000)
print(obj1)
""""
when ever we try to print object
print function  will internally called str function
whatever it return form str function 
"""

print("-----------------------------------------------------")





class Parent:
    parent = 101

    def __init__(self):
        self.j = 201
        print("--------Super Constructor-------")

    def superTest(self):
        print("---------Super Test---------")

    @staticmethod
    def staticMethod():
        print("---------Super Static Method---------")

    @classmethod
    def classMethod(cls):
        print("---------Super Class MEthod-----------")


class Child(Parent):
    child = 301

    def __init__(self):
        self.child = 401
        print("------Child Constructor---------")
        super().__init__()
        print(self.j)
        super().superTest()
        super().classMethod()
        super().staticMethod()

    def childTest(self):
        print("--------Child Test-------")
        super().superTest()
        print(c1.child)
        print(self.child)
        print(self.j)

    @classmethod
    def childClassMethod(cls):
        print("----------Child Class Method------------")
        super(Child,cls).superTest(cls)
        





c1 = Child()
c1.childClassMethod()
