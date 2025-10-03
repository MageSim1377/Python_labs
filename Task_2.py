str = input("Enter string: ")

newStr = str.replace('a', '').replace('u', '').replace('e', '').replace('i', '').replace('o', '')
newStr = newStr.replace('A', '').replace('U', '').replace('E', '').replace('I', '').replace('O', '')

print(newStr)