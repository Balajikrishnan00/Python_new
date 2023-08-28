student = {"rollNo": 5,
           "regNo": 1433005,
           "name": "Balaji",
           "DoB": "26-04-1997",
           "address": {
               "doorNo": 558,
               "street1": "kallarathinipatty",
               "post": "thirumalai(Post)",
               "talk": "sivaganga(Tk)",
               "district": "sivaganga(DT)",
               "Pincode": 630552},
           "languages": ["Python", "C", "C++", "Java"]
           }

print(student["name"])
student["age"] = 26
print(student)

del student["age"]
print(student)
student["location"] = (142244323.00, 34434344.00)
print(student)
print(student["address"])
for i, j in student["address"].items():
    print(f"{i} : {j}")
print("----------------------------------------")
for key, value in student.items():
    if isinstance(value, tuple) or isinstance(value, list):
        print(f"----------{key}----------")
        for i in value:
            print(i)
    elif isinstance(value, dict):
        print(f"----------{key}----------")
        for i, j in value.items():
            print(f"{i} : {j}")
    else:
        print(f"{key} : {value}")
