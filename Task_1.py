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

someAbsolutelyRandomListThatIDidNotTookFromTask = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]

flatifyList(someAbsolutelyRandomListThatIDidNotTookFromTask)

print(someAbsolutelyRandomListThatIDidNotTookFromTask)