import random

class StealingError(Exception):
    pass

class Bank:
    pass

class Customer: 
    accounts = {}

    def __init__(self):
        self.id = random.randint(1, 100000)
    
    def openAccount(self, currency):
        if currency in self.accounts.keys():
            raise ValueError("No-no-no, mister Custumer, you only can have one account in each currency")
        newAcc = Account(currency, cust)
        self.accounts[currency] = newAcc

    def closeAccount(self, currency):
        if currency not in self.accounts.keys():
            raise ValueError("No-no-no, mister Custumer, you have not any account in this currency")
        del self.accounts[currency]

    def income(self, amount, currency):
        try:
            self.accounts[currency].balance += amount
        except (KeyError):
            print("Man, you dont have account in this currency!")

    def outcome(self, amount, currency):
        try:
            if(self.accounts[currency].balance >= amount):
                self.accounts[currency].balance -= amount
            else:
                raise StealingError("Man, you have enough money, are you trying to rob us?")
        except StealingError:
            print("I am disappointed")

    


class Account:
    def __init__(self, cur, cust):
        self.balance = 0
        self.currency = cur
        self.customer = cust
        self
        pass
    pass

cust = Customer()
cust.openAccount("RAF")
print(cust.accounts["RAF"].balance)