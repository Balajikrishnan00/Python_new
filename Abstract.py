from abc import *


class Person(ABC):
    def __init__(self):
        print("Person Constructor")
    @abstractmethod
    def breakFast(self):
        pass


class Indian(Person):
    def __init__(self):
        print("Indian Constructor")


class Tamil(Indian):
    def __init__(self):
        print("Tamil Constructor")

    def breakFast(self):
        print("Itly")



#p1 = Person()
#i = Indian()

t= Tamil()


