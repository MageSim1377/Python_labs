password = input("Enter password: ")

def checkIsOnlyNumbers(str):
    flag = True
    for i in str:
        if ord(i) < ord('0') or ord(i) > ord('9'):
            flag = False
            break
    return flag

def checkIsOnlyLetters(str):
    flag = True
    for i in str:
        if ord(i) < ord('A') or ord(i) > ord('z'):
            flag = False
            break
    return flag

if len(password) < 16:
    print("Too short")
elif checkIsOnlyNumbers(password) or checkIsOnlyLetters(password):
    print("Weak password")
else:
    print("Strong password")