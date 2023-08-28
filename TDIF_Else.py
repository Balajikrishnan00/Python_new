"""
age = 17
if age >= 18:
    print("You can Vote!")
else:
    print("You cannot Vote!")

name = input("Enter your Name: ")
age = int(input("Enter Your age: "))
_form = input("From: ")
_to = input("To Where: ")

if age>18:
    if _form.lower() == "madurai"and _to.lower() =="chennai":
        ticket = 900
        print("ticket amount is: ",ticket)
    elif _form.lower() == "madurai"and _to.lower() =="thiruchy":
        ticket = 300
        print("Ticket amount is :",ticket)
if age<3:
    print("No Ticket")

cars = ["audi", "bmw", 'maruthi', 'honda']
i = "audi" or "bmw"
if i in cars:
    print(f"{i} luxury cars available")

poem = ""
line = ""
while line.lower() != "quit":
    line = input("Write: ")
    poem += line
    poem += "\n"
print(poem.replace("quit","")
"""
