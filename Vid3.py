import string

al = "abcdefghijklmnopqrstuvwxyz"
# print(al[0])
# print(al[len(al)-1])

# name = input("Enter Your Name: ")

print(al[len(al) - 1:len(al) - 1 - 5:-1])
print(al[len(al) - 1 - 4::])
print(al[-5:])

# slicing [startingPint:endingPoint:stepOperator]

print(al[::1])
print(al[::2])
print(al[::3])
print("-----------------------------")
# 1 remove Space
#name = input("Enter Name: ")
# res = name[0].upper() + name[1:-1] + name[-1].upper()
#length = int(len(name)/2)
#print(len(name))
#print(length)
#print(name[0:length] + name[length].upper() + name[length+1:])

# Type Casting

print(int(True))
print(int(False))
print(int(2.32))
print(int("20"))

print("------------------")
print(float("10.3"))
print(float("10"))
print(float(True))
print("----------------------------")
print(bool(0))
print(bool(0.0))
print(bool(0.1))
print(bool(1.0))
print(bool("B"))
print(bool(""))
print(bool(" "))
print("------------------------")
# String

print(str(12))
print(str(2.0))
print(str(True))
print(type(str(False)))

b1= "Balaji"
b2 = "Balaji"
print(id(b1))
print(id(b2))
b1 = "ba"
print(id(b1))

# no constant in python
# full Capital

# Escape character
print("---------------------------")
# Arithmetic Operator
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10%5)
print(10//5)
print(10**5)

# Relational Operator


# membership operator
sentance = "Chennai in capital of tamilnadu"

sentance = sentance.lower()
print(sentance)
print("chennai" in sentance)

# ternary Operator or conditional operator

a,b = 10,20
c = 30 if a>b else 40
print(c)

a,b,c = 101,200,300

min = a if a<b and a<c else b if b<c else c
max= a if a>b and a>c else b if b>c else c
print(min)
print(max)

# identity Operator
# memory operator --

print( a is a)


#name = input("enter name :")
#print(r'hi',name,"welcome")
#print("hi"+name+"welcome")

#num1 = int(input("enter num one:"))
#num2 = int(input("enter num two:"))
#print(type(num1))

# eval() operator
res = eval("10+20+30")
print(res)

#num = input("enter num:")
#print(eval(num))

import math

print(math.pi)