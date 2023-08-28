# Tuple is immutable, is it possible to keep change the value . Yes we can, If we keep the mutable object inside the
# tuple.

tup = ([1, 2, 3], 'myname')
tup[0][0] = [2]
print(tup[0])

print(tup[1])
print(tup)

"""
The tuple consists of a string and a list. 
Strings are immutable so we can’t change its value. 
But the contents of the list can change. 
The tuple itself isn’t mutable but contain items that are mutable. 
"""