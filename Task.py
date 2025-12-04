import random

class StealingError(Exception):
    pass

class IncorrectCustomerError(Exception):
    pass

class IncorrectAccountError(Exception):
    pass


class Bank:
    customers = {}
    pass

class Customer: 
    def __init__(self):
        self.accounts = {}
        self.id = random.randint(1, 100000)
        while self.id in Bank.customers.keys():
            self.id = random.randint(1, 100000)
        Bank.customers[self.id] = self
    
    def openAccount(self, currency):
        try:
            if currency in self.accounts.keys():
                raise ValueError()
            newAcc = Account(currency, self)
            self.accounts[currency] = newAcc
        except ValueError:
            print("No-no-no, mister Custumer, you can only have one account in each currency")

    def closeAccount(self, currency):
        try:
            if currency not in self.accounts.keys():
                raise ValueError()
            del self.accounts[currency]
        except ValueError:
            print("No-no-no, mister Custumer, you don't have any account in this currency")

    def income(self, amount, currency):
        try:
            self.accounts[currency].balance += amount
        except (KeyError):
            print("Man, you don't have account in this currency!")

    def outcome(self, amount, currency):
        try:
            if(self.accounts[currency].balance >= amount):
                self.accounts[currency].balance -= amount
                print(f"Take your {amount} {currency}, man")
            else:
                raise StealingError("You don't have enough money!")
        except StealingError:
            print("Man, you don't have enough money, are you trying to rob us? I am disappointed")
        except (KeyError):
            print("Man, you don't have account in this currency!")

    def transfer(self, amount, currency, reciever):
        try:
            if reciever not in Bank.customers.keys():
                raise IncorrectCustomerError()
            if currency not in Bank.customers[reciever].accounts.keys():
                raise IncorrectAccountError()
            if(self.accounts[currency].balance >= amount):
                self.accounts[currency].balance -= amount
                Bank.customers[reciever].accounts[currency].balance += amount
                print("Transaction approved!")
            else:
                raise StealingError()
        except IncorrectCustomerError:
            print(f"Customer with id {reciever} doesn't exist")
        except IncorrectAccountError:
            print(f"Customer with id {reciever} doesn't have account in {currency}")
        except StealingError:
            print("You don't have enough money!")
        pass
    


class Account:
    def __init__(self, cur, cust):
        self.balance = 0
        self.currency = cur
        self.customer = cust
        pass
    pass

cust = None
while True:
    print("1. Create customer\n2. Choose customer\n3. Print costomers\n")
    choose = int(input("Your choise: "))
    if choose == 1:
        cust = Customer()
        break
    elif choose == 2:
        try:
            cust = Bank.customers[int(input("Enter ID: "))]
            break
        except KeyError:
            print("There is no customer with that ID")
    elif choose == 3:
        for id in Bank.customers.keys():
            print(id)

while True:
    print("1. Open account\n2. Close account\n3. Deposit to account\n4. Withdraw from an account\n5. Transfer money\n" \
    "6. Print costomers\n7. Change customer\n8. New customer\n9. Report\n10. Report into file\n11. Exit\n")
    choose = input("Your choise: ")
    if choose == '1':
        currency = input("Enter currency: ")
        cust.openAccount(currency)
        pass
    elif choose == '2':
        currency = input("Enter currency: ")
        cust.openAccount(currency)
        pass
    elif choose == '3':
        currency = input("Enter currency: ")
        amount = int(input("Enter amount: "))
        cust.income(amount, currency)
        pass
    elif choose == '4':
        currency = input("Enter currency: ")
        amount = int(input("Enter amount: "))
        cust.outcome(amount, currency)
        pass
    elif choose == '5':
        currency = input("Enter currency: ")
        amount = int(input("Enter amount: "))
        cust2 = int(input("Enter ID you want to transfer to customer with: "))
        cust.transfer(amount, currency, cust2)
        pass
    elif choose == '6':
        for id in Bank.customers.keys():
            print(id)
        pass
    elif choose == '7':
        try:
            cust = Bank.customers[int(input("Enter ID: "))]
        except KeyError:
            print("There is no customer with that ID")
        pass
    elif choose == '8':
        cust = Customer()
        pass
    elif choose == '9':
        for cur, acc in cust.accounts.items():
            print(f"{cur}: {acc.balance}")
        print()
        
    elif choose == '10':
        with open(f"{cust.id}.txt", "w") as f:
            for cur, acc in cust.accounts.items():
                f.write(f"{cur}: {acc.balance}")
    elif choose == '11':
        break
    else:
        print("Incorrect choise")