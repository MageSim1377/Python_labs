class StealingException(Exception):
    pass


class Juwelry:
    def __init__(self, name = "Random juwelry", weight = 100, metal = "gold", price = 0, hasGems = False):
        self.name = name
        self.weight = weight
        self.metal = metal
        self.price = price
        self.hasGems = hasGems
        print("Juwelry forged!")

    def buy(self, money):
        try:
            if money > self.price:
                print(f"You bought {self.name}")
            else:
                raise StealingException()
        except StealingException:
            print("No-no-no, mister buyer, you don't have enough money!")

    def smelt(self):
        print(f"You got {self.weight} grams of {self.metal}")


class Ring(Juwelry):
    def __init__(self, name = "Ring", weight = 100, metal = "gold", price = 0, hasGems = False):
        super(Ring, self).__init__(name, weight, metal, price, hasGems)
        print("But all of them were decieved, as another ring was forged in the Doom Mountain, One Ring to rul them all")
    

class Pendant(Juwelry):
    def __init__(self, name = "Pendant", weight = 100, metal = "gold", price = 0, hasGems = False):
        super(Juwelry, self).__init__(name, weight, metal, price, hasGems)
        print("Pendant forged!")


juwelry = []

while True:
    print("""Make your choise:
             1. Create juwelry
             2. Print juwelry
             3. Bue juwelry
             4. Smelt juwelry
             5. Exit\n
          """)
    choise = int(input("Make your choise: "))
    if choise == 1:
        print("""Choose juwelry:
                 1. Ring
                 2. Pendant
                 3. Just juwelry
              """)
        juwChoise = int(input("Choose juwelry: "))
        if juwChoise == 1:
            juwelry.append(Ring())
        elif juwChoise == 2:
            juwelry.append(Pendant())
        elif juwChoise == 3:
            juwelry.append(Juwelry())
    elif choise == 2:
        for j in juwelry:
            print(j.name, '\n')
    elif choise == 3:
        index = int(input("Enter index: "))
        money = int(input("Enter money: "))
        juwelry[index].buy(money)
        juwelry.pop(index)
    elif choise == 4:
        index = int(input("Enter index: "))
        j.smelt()
        juwelry.pop(index)
    else:
        break
    