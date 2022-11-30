class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if (amount > self.balance):
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else:    
            self.balance = self.balance - amount

    def display_account_info(self):
        print(f"{self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance + (self.balance * self.int_rate)

BobsAccount = BankAccount(0.01, 9850)
StevesAccount = BankAccount(0.05, 82500)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def display_account_info(self):
        self.account.display_account_info
        print(f"{self.balance}")

bob = User("Robert Paulson", "bobpaulson@comcast.net")
fred = User("Freddie Savage", "fredsavage@yahoo.com")

fred.make_deposit(100)
bob.make_withdrawal(1000)
fred.display_account_info

