def greet(name="Anonymous"):
    print(f"welcome MR.{name}")


#username = input("Enter your name: ")
greet()


def user():
    print("hello world")


user()


def calculate_add(a, b):
    print(a + b)


calculate_add(10, 30)


def greet_users(greet_message, user):
    print("%s, %s" % (greet_message, user))
    print("{}, {}".format(greet_message, user))
    print(f"{greet_message}, {user}")


greet_users("Welcome", 'balaji')

