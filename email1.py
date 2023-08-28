# python list vs tuple vs dictionary vs set vs array

# mutable and immutable in python object

# How to change mutable to imputable
# How to find is it mutable or not


list1 = [1, 2, 3, 10, 3, 4, 5, 1, "Balaji"]
# list is mutable
# list has indexing
# position insert

l1 = [i * i for i in range(1, 11)]

print(l1)

tuple1 = (1, 3, 4, 1, 2, 4, 2, 1, 3, "Balaji")
# 'tuple' object does not support item assignment
# tuple has indexing
# tuple is immutable

dict1 = {"name": "balaji", "number": 12345}
# dict is mutable
# dict key pair value
#

set1 = {1, 2, 4, 1, 2, 4, 3, 1, 4, 3}
# will remove duplicate value
set1.add(10)
print(set1)

# ------------------------------------------------
print(list1)
print(tuple1)
print(dict1)
print(set1)
# -----------------------------------------------
print(list1[:3])
print(tuple1[:4])

# --------------------------------------------
t1 = (10, 20, 30, 10)
t2 = (10, 40, 50)
t3 = t1 + t2
print(t3)
t4 = t3 * 2
print(t4)
print(len(t4))
print(t4.count(10))
# print(t4.index(0))
print(min(t4))
print(max(t4))
print(sum(t4))

# tuple Packing unpacking
a, b, c, d = 10, 20, 30, 40
t = a, b, c, d
print(t)
p, q, r, s = t
print()
t5 = (100, 90, 80, 70)
a1, b1, c1, d1 = t5
print(a1)
# tuple Comprehension
t6 = (i * i for i in range(1, 10))
print(type(t6))

# a1 = eval(input("enter value: "))
# print(type(a1))
# print(a1)
# for i in a1:
#    print(i)
print("---------------SET----------------------")
# Set : Mathematical set
# no duplicate allowed
# no order maintain
# set object are mutable
# no indexing
# intersection
# union
# difference


s1 = {10, 20, 30, 40}
print(s1)
s2 = set(t1)
print(s2)

s3 = set(range(5))
print(s3)

l = list()
s = set()
t = tuple()
d = dict()
print(type(l), type(s), type(t), type(d))

name = "Balaji"
n1 = tuple(name)
print(n1)

s.add(100)
print(s)
s.add(101)
print(s)
s.update(l1)
print(s)
s.update(n1)
print(s)
s.add("Balaji")
print(s)
c = s.copy()

print("copy:", c)

# print(c.pop())
# print(c.pop())
# print(c.pop())
# print(c.pop())
print(c.remove(64))  # KeyError
print(c)
print(type(c))

# discord
print(s.discard(11111))
print(s)

# intersection
# union
# difference

s10 = {10, 20, 30, 40, 50}
s11 = {10, 30, 50, 70}

print(s10.intersection(s11))
print(s10.union(s11))
print(s10.difference(s11))
print("-----------------------")
print(s10 | s11)
print(s10 & s11)
print(s10 - s11)
print(s10 ^ s11)
# frozenset
s12 = frozenset(s10)
print(s12)
print(type(s12))

