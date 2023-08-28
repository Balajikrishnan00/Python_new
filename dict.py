d = dict()
d["name"] = "Balaji"
d["age"] = 26
d["name"] = "Ba"

print(d)

trainDetails = dict()

for i in range(1, 10):
    trainDetails["TA" + str(i)] = i
print(trainDetails)

# del

del trainDetails["ta1".upper()]
print(trainDetails)

# del  trainDetails
print(trainDetails)

# no duplicate key
# no order no slicing no indexing
# mutable
print(len(trainDetails))
# delete
# trainDetails.clear()
print(trainDetails)

print(trainDetails.get("Ta2".upper()))
print(trainDetails["ta2".upper()])

print(trainDetails.pop("ta3".upper()))
print(trainDetails)

popitem = (trainDetails.popitem())
print(type(popitem))

for i in popitem:
    print(i)

d1 = {"name": "Balaji", "age": 50}
print(d1.get("name"))
print(d1.get("salary"))
print(d1.get("salary", 0))

# d2 = eval(input("Dictionary:"))
# print(d2)

register = dict()

# noS = int(input("No of Student: "))
# for i in range(noS):
#    subjectName = input("Enter a subject name: ")
#    mark = int(input("Enter a mark: "))
#    register[subjectName] = mark

# print(register)

l1 = ["tamil", "english", "maths", "science", "social"]
l2 = [90, 67, 79, 87, 96]

studentMarks = dict()

for i in range(len(l1)):
    studentMarks[l1[i]] = l2[i]

print(studentMarks)

studentMarks = {value: key for key, value in studentMarks.items()}
print(studentMarks)

studentMarks2 = dict()

for key, value in studentMarks.items():
    studentMarks2[value] = key
print(studentMarks2)

employee1 = {"balaji": 100000, "ravi": 10000, "kuna": 12000, "siva": 50000}
for name, salary in employee1.items():
    if salary >= 25000:
        print(name, salary)

empkeys = list(employee1.keys())
print(list(employee1.keys()))
print(sorted(list(employee1.values())))

print(sorted(employee1.items()))

# bubble sorting


l1 = [10, 1, 8, 4, 9, 5]

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]
print(l1)

l = [i for i in range(1, 32)]
print(l)
min = 0
max = len(l) - 1
# print(avg)
mind = 5
i = 0
"""
while True:
    avg = min + max // 2
    if mind == l[avg]:
        print(avg)
        print(i)
        break
    elif mind < l[avg]:
        min = avg + 1
        avg = min + max // 2

    else:
        min = avg - 1

    i += 1
"""
d = {}
name = input("Enter a Name: ")
for i in name:
    d[i] = name.count(i)
print(d)

c = {i: name.count(i) for i in name}
print(c)
