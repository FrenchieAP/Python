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
BobsAccount.deposit(100)
BobsAccount.deposit(250)
BobsAccount.deposit(50)
BobsAccount.withdraw(250)
BobsAccount.yield_interest()
BobsAccount.display_account_info()
StevesAccount.deposit(500)
StevesAccount.deposit(1500)
StevesAccount.withdraw(500)
StevesAccount.withdraw(500)
StevesAccount.yield_interest()
StevesAccount.display_account_info()




