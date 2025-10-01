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
        unique += str(i) + " "

print(f"Unique numbers: {unique}")

repeating = ""

for i in numDict.keys():
    if numDict[i] != 1:
        repeating += str(i) + " "

print(f"Repeating numbers: {repeating}")

even = ""
odd = ""

for i in numDict.keys():
    if i % 2 == 0:
        even += str(i) + " "
    elif i % 1 == 0:
        odd += str(i) + " "

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")

negative = ""

for i in numDict.keys():
    if i < 0:
        negative += str(i) + " "

print(f"Negative numbers: {negative}")

floatNums = ""

for i in numDict.keys():
    if i % 1 != 0:
        floatNums += str(i) + " "

print(f"Float numbers: {floatNums}")

divisibleBy5 = ""

for i in numDict.keys():
    if i % 5 == 0:
        divisibleBy5 += str(i) + " "

print(f"Divisible by 5 numbers: {divisibleBy5}")

for i in numDict.keys():
    if i % 1 != 0:
        floatNums += str(i) + " "

print(f"Biggest number: {max(numDict.keys())}")
print(f"Smallest number: {min(numDict.keys())}")