listStr = input("Enter some list: ")

someList = listStr.split()

newList = []

for i in someList:
    if not i in newList:
        newList.append(i)

print(newList)