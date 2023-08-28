# Python -> High Level Language Programing
# Dynamically Type Language
# General Purpose
# Programing Language
# 1989 Guido van Rossam


name = 'balaji'
print(name[0])
print(name)
# name =input("Enter Your Name: ")
print(name)

print(dir(str))

# print(tamil + english)

tamil, english, maths, science, social = 94, 89, 100, 81, 91
total = tamil + english + maths + science + social
print(total)
percentage = total / 3
print(round(percentage, 1))

# Identifier:
tamil, english, maths, science, social = 94, 89, 100, 81, 91
print(tamil)

myName = "Balaji"
fatherName = "Krishnan"
print(fatherName[1:5])
total = tamil + english + maths + science + social
print(total)
tamil = english = maths = 90, 98, 98
print(tamil, english, maths)

import keyword

kw = keyword.kwlist
print(len(kw))
for i in kw:
    print(i)

print(round(12.6))

print(complex(5 + 10j) + 10 + 8j)

# int, float String,Bool,raw string

name = "Balaji"
age = 26
weight = 50.5
height = 152

# escape character

n1 = r"I'm from India"
print(n1)
n2 = '''I'm India'''
print(n2)

# String Slice
# Indexing
name = "Balaji from india"
print(name[0])
a = 0
for i in name:
    if i == "a":
        a += 1

    print(i, end="- ")
# print(a)

# print(name[::-1])

# p = input("Enter Password: ")

al = r"abcdefghijklmnopqrstuvwxyz"
print(al)

