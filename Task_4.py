money = int(input("Enter amount of money: "))

if money // 100 > 0:
    print(str(money // 100) + " banknotes of 100 rubles") 
    money %= 100
if money // 50 > 0:
    print(str(money // 50) + " banknotes of 50 rubles") 
    money %= 50
if money // 10 > 0:
    print(str(money // 10) + " banknotes of 10 rubles") 
    money %= 10
if money // 5 > 0:
    print(str(money // 5) + " banknotes of 5 rubles") 
    money %= 5
if money // 2 > 0:
    print(str(money // 2) + " coins of 2 rubles") 
    money %= 2
if money // 1 > 0:
    print(str(money // 1) + " coins of 1 rubles") 
    money %= 1