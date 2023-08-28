"""
s1 = "pto"
s2 = "yhn"
i, j = 0, 0
join = ""
while i < len(s1) or j < len(s2):
    if i < len(s1):
        join += s1[i]
        i += 1
    if j < len(s2):
        join += s2[j]
        j += 1
print(join)


# input : a5b6c7d8
# output: abc5678

input = "a5b6c7d8"
output1 = ""
output2 = ""
i = 0
while i < len(input):
    if input[i].isalpha():
        output1 += input[i]
    if input[i].isdigit():
        output2 += input[i]
    i += 1
print(output1 + output2)

"""
# input  :A55
# output: AAAAA

s1 = "Balaji"
s1[0] = "k"
if s1[0] == "B":
    s1[0] = "K"

print(s1)
