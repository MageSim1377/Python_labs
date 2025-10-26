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

cust1 = Customer()
cust2 = Customer()
cust1.openAccount("RAF")
cust2.openAccount("RAF")
cust1.income(500, "RAF")
cust1.transfer(200, "RAF", cust2.id)