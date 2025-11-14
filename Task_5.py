word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

letters1 = []
letters2 = []

letters1.extend(word1.lower())
letters2.extend(word2.lower())

for i in range(len(letters1)):
    for j in range(len(letters1) - 1):
        if letters1[j] < letters1[j + 1]:
            t = letters1[j]
            letters1[j] = letters1[j + 1]
            letters1[j + 1] = t

for i in range(len(letters2)):
    for j in range(len(letters2) - 1):
        if letters2[j] < letters2[j + 1]:
            t = letters2[j]
            letters2[j] = letters2[j + 1]
            letters2[j + 1] = t

flag = True

if len(letters1) != len(letters2):
    flag = False
else:
    for i in range(len(letters1)):
        if letters1[i] != letters2[i]:
            flag = False
            break

if flag == True:
    print("Yes")
else:
    print("No")