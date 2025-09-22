string = input("Enter string: ")

startIter = 0
endIter = len(string) - 1

flag = True

while startIter < endIter:
    if string[startIter] != string[endIter]:
        flag = False
        break
    else:
        startIter += 1
        endIter -= 1

if flag:
    print("Yes")
else:
    print("No")