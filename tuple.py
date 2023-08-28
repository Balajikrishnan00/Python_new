from random import random

t = [ i for i in range(1,10)]
t = (1, 2, 3, 4, 5, 6,6, 7, 8, 9)
print(t)
print(t[:])
print(t[:])
print(t.count(6))

l1 = [i for i in range(10)]
print(l1)
print(l1.append(10))
l1 = tuple(l1)
print(type(l1))
print(l1)
l1 =list(l1)
print(type(l1))


t1 = ([1,2,3],"Balaji")
print(t1)
t1[0][0] = 2
t1[0][1] = 3
t1[0][2] = 4

print(t1)




