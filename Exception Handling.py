"""
try:
    n1 = int(input(":"))
    n2 = int(input(":"))
    print(n1 / n2)


# except (ZeroDivisionError,ValueError) as meg:
except:
    print("Error")
finally:
    print("finally")

print("welcome")


def divison():
    try:
        n1 = int(input(":"))
        n2 = int(input(":"))
        return (n1 / n2)
    except ZeroDivisionError:
        print("ZeroDivisionByError")
        divison()
    except ValueError as meg:
        print("Error")
        divison()
    print("welcome")


# divison()
"""


# User Defined Exception

class InsufficientBalance(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


balance = 1000
try:
    amount = int(input("Enter  Amount:"))
    if amount > balance:
        raise InsufficientBalance("InsufficientBalance")
    print("Collect Your Cash...")
except InsufficientBalance:
    print("Check your Balance")



