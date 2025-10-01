str = input("Enter string: ")

newStr = ""

for el in str:
    i = el.lower()
    if i != 'a' and i != 'o' and i != 'i' and i != 'e' and i != 'u':
        newStr += el

print(newStr)