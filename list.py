"""
bikes = ['ktm', 'yamaha', 'Tvs']
numbers = [i for i in range(1, 11)]
bikes.append("honda")
bikes.insert(0,'bajaj')

# numbers.clear()
numbers2 = numbers.copy()
numbers.clear()
numbers2.extend([12,13,14,16,15])
numbers2.sort(reverse=True)
print(numbers2.index(16,))
pop = numbers2.pop()
print(bikes)
print(numbers2)
print(pop)


l1 = ["BALAJI", 123, ]
print(l1[0][len(l1[0]) - 1])

name = "Balaji"
l2 = list(name)
print(l2)

l3 = list(range(1, 10))
print(l3)

l4 = str(l2)
print(l4)

sen = "happy new Year"
print(sen.split(" "))

for i in sen:
    if i != ' ':
        print(i.split())


input = "sun mon tues wedness thus fri satur".split()
lis2 = []
for i in input:
    lis2.append(i+"day")
print(input)
print(lis2)

for i in input:
    if i.endswith('s'):
        print("------",i)

for i in input:
    if len(i)>=4:
        print(i)

#input = " ".join(lis2)
#print(input)
#print(type(input))


l1 = [10,40,50,20]
l2 = l1

print(l1 is l2)
print(id(l1),id(l2))


#python_student = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

records = []
N = int(input("Enter number of student: "))
for i in range(N):
    list1 = []
    record = input("enter student Name:")
    score = float(input("enter a score"))
    list1.append(record)
    list1.append(score)
    records.append(list1)


l1 = ["balaji", 50.9]
l2 = ["time", 51.0]
print(l1 > l2)
l3 = []
l3.append(l1)
l3.append(l3)

print(l3[0])
print(len(l3))
print(l3.count(object))

namesOnly = ["balaji", "siva", "kumar", "anu"]
timeOnly = [9.0, 9.0, 18.9, 15]
i = 0
studentList = []
while i < len(namesOnly) or i < len(timeOnly):
    studentList.append([namesOnly[i], timeOnly[i]])
    i += 1
-------------------
studentList = []
for i in range(int(input())):
    l1 = input()
    l2 = float(input())
    studentList.append([l1,l2])
sorted(studentList)
i, j = 0, 1
while i < len(studentList):
    while j < len(studentList):
        if studentList[i][1] > studentList[j][1]:
            studentList[i], studentList[j] = studentList[j], studentList[i]
        j += 1
    i += 1
print(studentList)
i=0
while i<2:
    print(studentList[i][0])
    i+=1
"""
score_list = {}
print(type(score_list))
for i in range(int(input())):
    name = input()
    score = float(input())
    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]

new_list = []
for i in score_list:
    new_list.append([i, score_list[i]])

new_list.sort()
result = new_list[1][1]
result.sort()
print(*result, sep="\n")
