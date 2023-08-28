"""
# datatypes
1) string
2) float
3) bool
4) numbers
# collections
1) list
2) tuple
3) set
4) Dictionaries
5) file
#-------------------------------------

# string
s1 = "python"
print(id(s1))
s1.replace("on","off")
print(s1)
print(id(s1))
print(s1)
s1.replace("py","cy")
print(s1)
s1=("python").replace("p","B")
print(s1.swapcase())
#-----------------------------------
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))
print(round(6.5))
print(round(7.5))
print(round(8.5))
print(round(9.5))
print(round(10.5))
print(round(11.5))
print(round(12.5))
print(round(13.5))
print(round(14.5))
print(round(15.5))
print(round(16.5))
print(round(17.5))
#------------------------------------------

# string Methods
p1 = "\tpython\t"
print(p1.index("on"))

p1 = p1.strip().capitalize().swapcase().capitalize()

print(p1*3)
"""
# ----------------------------------------
print("Hello World!")
message = "Hello World!"

print(message)

s1 = ["Balaji", 152, 55.0, "true"]
print(s1)
languages = ["Java","c","c++","python","javascript"]
languages1 = []
for i in languages:
    languages1.append(i.capitalize())
languages.clear()
languages=languages1.copy()
print(languages)

print(languages[0])
print(languages[1].upper())
languages.append("c#".upper())
print(languages)
print(languages.pop())
print(languages[::-1])
print(languages.pop())
print(languages)
languages.extend(["R","Go"])
print(languages)
del languages[-1]
print(languages)
languages.sort()
print(languages)
languages.insert(0,"Kotlin")
print(languages)
removeLanguage=languages.pop(-1)
print(removeLanguage)
print(languages)
print("-----------------------------------")
print(languages)
languages.remove("Kotlin")
print(languages)
languages.reverse()
print(languages)
languages.sort()
print("------------------------------------")
nums = [10,20,100,23,1,9,13,8]
nums.reverse()
print(nums)