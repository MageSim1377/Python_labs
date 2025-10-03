day = int(input("Enter day of your birth: "))
month = int(input("Enter month of your birth: "))

if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print(f"{day}.{month} is aquarius")
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print(f"{day}.{month} is pisces")
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print(f"{day}.{month} is aries")
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print(f"{day}.{month} is taurus")
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    print(f"{day}.{month} is gemini")
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    print(f"{day}.{month} is cancer")
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print(f"{day}.{month} is leo")
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print(f"{day}.{month} is virgo")
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print(f"{day}.{month} is libra")
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print(f"{day}.{month} is scorpio")
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print(f"{day}.{month} is sagittarius")
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print(f"{day}.{month} is capricorn")
else:
    print("Uncorrect date")
