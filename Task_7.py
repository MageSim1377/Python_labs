def mergeSortedLists(list1, list2): #for lists that are sorted in ascending order
    newList = []
    i1 = 0
    i2 = 0
    while i1 < len(list1) or i2 < len(list2):
        if(i1 != len(list1) and (i2 == len(list2) or (list1[i1] < list2[i2]))):
            newList.append(list1[i1])
            i1 += 1
        else:
            newList.append(list2[i2])
            i2 += 1
    return newList

list1 = [1, 3, 5, 7, 9, 11, 11, 11]
list2 = [2, 2, 2, 2, 4, 6, 8, 10, 10, 10, 10]

print(mergeSortedLists(list1, list2))