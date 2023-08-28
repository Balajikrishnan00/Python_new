def sayHello1():
    return "Good Morning"


def sayHello(user, greet):
    return f"{greet}, MR.{user}"


username = input("Enter UserName: ")
greet = sayHello1()
print(sayHello(username.title(), greet))
