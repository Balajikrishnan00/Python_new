languages = ["Java", "c", "c++", "python", "javascript"]

for i in languages:
    print(f"{i} length of {len(i)}")

a = {10, 20, 30, 40, 50, 60, 70, 80, 90,80}
print(type(a))
print(a)

for i in languages:
    if i.lower() == "c":
        i.upper()
