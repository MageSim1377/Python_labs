numberStr1 = input("Enter first list of nunmbers: ")
numberStr2 = input("Enter second list of nunmbers: ")

numSet1 = {i for i in numberStr1.split()}
numSet2 = {i for i in numberStr2.split()}

print(f"Numbers in both lists: {numSet1 | numSet2}")
print(f"Numbers in first but not in second list: {numSet1 - numSet2}")
print(f"Numbers in second but not in first list: {numSet2 - numSet1}")
print(f"Numbers that only present in one of lists: {numSet1 ^ numSet2}")

#numSet1 = numberStr1.split()
#numSet2 = numberStr2.split()

#intersection = []
#firstWithoutSecond = []
#secondWithoutFirst = []
#unionWithoutIntersection = []

#for i in numSet1:
#    if i in numSet2:
#        intersection.append(i)
#    if not i in numSet2:
#        firstWithoutSecond.append(i)

#for i in numSet2:
#    if not i in numSet1:
#        secondWithoutFirst.append(i)

#unionWithoutIntersection = firstWithoutSecond + secondWithoutFirst

#print(f"Numbers in both lists: {intersection}")
#print(f"Numbers in first but not in second list: {firstWithoutSecond}")
#print(f"Numbers in second but not in first list: {secondWithoutFirst}")
#print(f"Numbers that only present in one of lists: {unionWithoutIntersection}")
