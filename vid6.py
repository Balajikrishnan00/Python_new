"""
total = int(input("Enter Your Mark: "))
if (total>=400) & (total<=500):
    print("Great")
    mark1 = int(input("Enter Your Tamil Mark: "))
    if mark1 >=80:
        print("great")
    else:
        print("okay")


#-------------------------------------------------------------------
total = int(input("Enter a Total: "))
if total > 500:
    while total > 500:
        total = int(input("Total"))
        if total > 500:
            continue
        else:
            if total >= 450:
                print("Wow")
                tamil = int(input("enter Tamil Mark: "))
                if tamil >= 90:
                    print("Wow super")
                else:
                    print("Nice")

else:
    if total >= 450:
        print("Wow")
        tamil = int(input("enter Tamil Mark: "))
        if tamil >= 90:
            print("Wow super")
        else:
            print("Nice")


#------------------------------------------
Cmind = 500
guess = 0
while guess!=Cmind:
    guess = int(input("Enter Your Guess:"))
    if guess == Cmind:
        print("Super")
    elif(guess>Cmind):
        print("Too Big")
    else:
        print("Too SMall")

n = int(input("Enter a Number: "))
i = 1
while i <= n:
    print(i)
    i += 1
print("-----------------------")
for i in range(1, n + 1):
    print(i)

print("-----------------------")

while(n>0):
    print(n, end=" ")
    n-= 2
    print(end= " ")
print("-----------------------")


n = int(input("MaxNumber:"))
count = 3
while(count<=n):
    print(count,end=" ")
    count*=3



endValue = int(input("MaxNumber:"))
startValue=1
while(startValue<=endValue):
    if startValue%3 ==0:
        print(startValue)
    startValue+=1


endValue = int(input("MaxNumber:"))
startValue = 1
while startValue <= endValue:
    if (startValue % 2 == 0) or (startValue % 3 == 0):
        print(startValue)
    startValue += 1

days=5
totalAmount =0
amount =0
while(amount<=100):
    totalAmount+=amount
    print(totalAmount)
    amount+=1
print(totalAmount)

name = input("Enter name:")
#print(len(name))
i=0
while(i<len(name)):
    if(name[i]=="a"):
        print(name[i])
    #print(name[i])
    i+=1


sentance = " balaji  chennai"
lenth = len(sentance)-1
#print(lenth)
i = 0
word = 0
while i < lenth:
    if sentance[i] == " ":
        if sentance[i+1]>="a" and sentance[i+1]<="z":
            #print("space available")
            word+=1
    #print(i)
    i += 1
print(word)

import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.capwords("balaji-welcome-python",sep="-"))
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.printable)
print(string.punctuation)
print(string.whitespace)
sen = "Python  Is a easy"
print(sen.find('a',12))



#print(email[0].upper()+email[1:email.index("@")])

#email = input("enter Email: ")


# tables

startNumber = 1
tableNumber = 5
endNumber = 20

while startNumber<=endNumber:
    print(f"{startNumber} *{tableNumber} = {startNumber*tableNumber}")
    startNumber += 1


subjects =[]
i=1
while i<=5:
    subject = int(input("Enter Subjects: "))
    subjects.append(subject)
    i+=1
print(subjects)
print(type(subjects))

"""
name = []
print(type(name))
name.append(1)
name.append(5)
name.insert(1,10)
print(name)

