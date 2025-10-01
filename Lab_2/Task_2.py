numbers = input("Enter some numbers you want to enter right now right here: ")

nums = numbers.split()

numDict = {}

for i in nums:
    if '.' in i:
        i = float(i)    
    else:
        i = int(i)
    if i in numDict.keys():
        numDict[i] += 1
    else:
        numDict[i] = 1

unique = ""

for i in numDict.keys():
    if numDict[i] == 1:
        unique += i + " "

print(f"Unique numbers: {unique}")

repeating = ""

for i in numDict.keys():
    if numDict[i] != 1:
        repeating += i + " "

print(f"Repeating numbers: {repeating}")

even = ""
odd = ""

for i in numDict.keys():
    if i % 2 == 0:
        even += i + " "
    else:
        odd += i + " "

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")