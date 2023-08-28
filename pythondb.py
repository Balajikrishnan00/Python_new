import sqlite3
import mysql.connector

con = mysql.connector.connect(database="")
tableName = "Python users".lower()


def insert(firstname, lastname, username, password):
    pass


def update(firstname, lastname, username, password):
    pass


def delete(id):
    pass


def select():
    curser = con.cursor()
    sql = "SELECT ID,Firstname,lastname,username,password FROM python users"
    curser.execute(sql)
    result = curser.fetchone()
    print(result)


prompt = "1. Insert Data\n2. Update Data\n3. Select Data\n4. Delete Data\n5. Exit\nEnter Your Choice :"
while True:

    choice = int(input(prompt))

    if choice == 1:
        firstname = input("FirstName: ")
        lastname = input("LastName: ")
        username = input("Username:")
        password = input("Password: ")
        insert(firstname, lastname, username, password)

    elif choice == 2:
        firstname = input("FirstName: ")
        lastname = input("LastName: ")
        username = input("Username:")
        password = input("Password: ")
        update(firstname, lastname, username, password)

    elif choice == 3:
        select()

    elif choice == 4:
        id = int(input("Enter ID to DELETE: "))
        delete(id)

    elif choice == 5:
        quit()
    else:
        print("Invalid Selection")
        continue
