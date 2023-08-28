with open("D:\\file.txt", "r") as file:
    if file:
        readLines = file.readlines()
        # print(type(readLines))
        # print(readLines)
        s1 = str()
        # print(type(s1))
        # print(s1.split(" "))
        for i in readLines:
            s1 += i
        print(s1)
        print(s1)
        print(s1.split(" "))
