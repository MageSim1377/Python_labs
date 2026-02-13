def flatifyList(someList):
    i = 0
    while i < len(someList):
        if isinstance(someList[i], list):
            newEl = flatifyList(someList[i])
            someList.remove(someList[i])
            for j in range(len(newEl)):
                someList.insert(i, newEl[len(newEl) - 1 - j])
        i += 1
    return someList

def getUniqueElements(someList):
    flatifyList(someList)
    newList = []
    for i in someList:
        if not i in newList:
            newList.append(i)
    return newList

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]

print(getUniqueElements(list_a))