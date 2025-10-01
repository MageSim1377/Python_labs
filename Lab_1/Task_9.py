string = input("Enter string: ")

flag = True

if len(string) != 15:
    flag = False
elif string[3] != '.' or string[7] != '.' or string[11] != '.':
    flag = False

for i in range(15):
    if i != 3 and i != 7 and i != 11 and (ord(string[i]) < ord('0') or ord(string[i]) > ord('9')):
        flag = False
        break
if flag:
    print("It is IP")
else:
    print("It is not IP")