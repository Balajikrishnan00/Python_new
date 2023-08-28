"""
def wish(name, message):
    print(name, message)


# positional arguments
# keyword arguments
# default arguments
# variable length arguments


wish("balaji", "welcome")

# positional  and keyword arguments
wish("balaji", message="welcome")


# first positional arguments then keyword arguments


def wish1(name="admin", message="welcome"):
    print(name, message)


wish1("Balaji")
wish1("good morning")
wish1()


def calculateTotal(*n):
    print(type(n))
    total = 0
    for sub in n:
        total += sub
    print(total)


calculateTotal(10, 20, 30, 40, 50)


def totalCalculate(**n):
    print(type(n))
    print(sum(n.values()))


totalCalculate(tamil=90, english=80)

# ----------------------------------------------------------------

discount = 20


def opTime():
    global discount
    discount = 30
    # print(discount)


def buyTv():
    print(discount)


def buyLaptop():
    discount = 25
    print(globals()["discount"])
    print(discount)


buyTv()
opTime()
buyTv()
print("----------------")
buyLaptop()

print("---------------------------------")

list1 = [1, 3, 5, 7, 9]
list2 = list()
for i in list1:
    for j in list1:
        list2.append(i * 10 + j)

print(list2)

# recursion

def Login(username, password):
    if username.lower() != "abcd":
        print("incorrect")
        username = input("Enter username: ")
        password = input("Enter password: ")
        Login(username, password)
    elif password.lower() != "abcd":
        username = input("Enter username: ")
        password = input("Enter password: ")
        Login(username, password)


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    Login(username, password)


login()



def fact(n):
    if n == 0:
        return 1
    else:
        return n + fact(n - 1)


# lamda functions
# 1) filter()
# 2) map()
# 3) reduce()

print(fact(5))

r1 = lambda a, b: a + b
r2 = lambda a: a * a

print(r1(10, 20))
print(r2(10))

r3 = lambda a, b: a if a > b else b
print(r3(10, 20))

print(type(r1(10, 20)))

"""


def openFridge():
    print("Door is opened")

    def lightOn():
        print("light is ON")

    lightOn()

# openFridge()
