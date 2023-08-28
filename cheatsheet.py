"""
print("hello world")

message= "Hello world"
print(message)

first_name = 'albert'
last_name = 'einstein'
full_name = first_name + ' ' + last_name
print(full_name)
"""
bikes = ["yamaha", "Tvs", "honda"]
print(bikes)
print(bikes[1])
print(bikes[-1])
print(bikes[:2])
bikes.append("bajaj")
print(bikes)
bikes.insert(0, "ktm")
print(bikes)

square = []
for x in range(1, 11):
    square.append(x ** 2)
print(square)
print("--------------------")

list1 = [i ** 2 for i in range(1, 11)]
print(list1)

t1 = tuple(list1)
print(t1)
print(type(t1))
print(t1[0])
print(t1[-1])
print(t1[1:])
res = "yamaha" in bikes
print(not res)
