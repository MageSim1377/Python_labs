abits = {}

def f1():
    surname = input("Enter surname: ")
    status = input("Enter status: ")
    mathMark = int(input("Enter math mark: "))
    phisicsMark = int(input("Enter phisics mark: "))
    langMark = int(input("Enter language mark: "))
    abits[surname] = [status, mathMark, phisicsMark, langMark]
    print("Abiturient added succesfully!\n")

def f2():
    surname = input("Enter surname: ")
    abits.pop(surname)
    print("Abiturient deleted succesfully!\n")

def f3():
    surname = input("Enter surname: ")
    subj = int(input("Chose suubject:\n1. Math\n2. Phisics\n3. Language\n"))
    mark = int(input("Enter new mark: "))
    if surname not in abits.keys():
        print("Incorrect")
        return
    abits[surname][subj] = mark    

def f4():
    surname = input("Enter surname: ")
    st = input("Enter new status: ")
    if surname not in abits.keys():
        print("Incorrect")
        return
    abits[surname][0] = st  
    pass

def printAbits():
    for key, value in abits.items():
        print(f"{key}:\n    Status: {value[0]}\n    Math: {value[1]}\n    Phisics: {value[2]}\n    Language: {value[3]}")

def printToFile():
    file = open("text.txt", "w")
    for key, value in abits.items():
        file.write(f"{key}:\n   Status: {value[0]}\n   Math: {value[1]}\n   Phisics: {value[2]}\n   Language: {value[3]}\n")

while True:
    print("1. Add abiturient\n2. Delete abiturient\n3. Change mark\n4. Change status\n5. Print\n6. Print to file\n7. Exit")
    choise = int(input("Make your choise that will determine your destiny: "))
    if choise == 1:
        f1()
    elif choise == 2:
        f2()
    elif choise == 3:
        f3()
    elif choise == 4:
        f4()
    elif choise == 5:
        printAbits()
    elif choise == 6:
        printToFile()
    elif choise == 7:
        break
    else:
        print("Your choise is incorrect!")
