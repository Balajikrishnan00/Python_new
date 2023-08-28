def decorateDivision(func):
    print(type(func))

    def innerDivision(no1, no2):
        if no2 == 0:
            return "check no2"
        return func(no1, no2)

    return innerDivision


@decorateDivision
def division(no1, no2):
    return no1 / no2


print(division(0, 121212))


def dooropen():
    def lightOn():
        print("light is oN")

    lightOn()
    return "door is opened"


def doorClose():
    def lightOff():
        print("Light OFF")

    lightOff()
    return "Door is closed"


print(dooropen.__call__())
# print(dooropen())
print(doorClose)


# extending functionality of an exiting function, without modifying it.
# -----------------------------------------------------------------

# generator functions
# it generate sequence of value


def test():
    yield "a"
    yield "b"
    yield "c"
    yield "d"


result = test()
print(result.__next__())
print(next(result))
print(type(result))


def Nnumbers(num):
    n = 1
    while n <= num:
        yield n
        n += 1


value = Nnumbers(10)
for i in value:
    print(i)
# -----------------------------------------------
print("_________________________________________")


def my_decorator(some_fun):
    def wrapper():
        print("before some_function() is called.")
        some_fun()
        print("after some_function() is called.")

    return wrapper


@my_decorator
def just_some_function():
    print("Wheee!")


just_some_function()
