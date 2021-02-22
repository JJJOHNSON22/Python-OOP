class BankAccount:
    def __init__(self, balance, int_rate):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Balance: {self.balance}, Interest Rate: {self.int_rate}')
        return self
    def yield_interest(self):
        self.balance = (((self.int_rate / 12) * self.balance) * 100) + self.balance
        return self

account1 = BankAccount(0, 0.05)
account2 = BankAccount(0, 0.05)

account1.deposit(500).deposit(50).deposit(150).withdraw(250).yield_interest().display_account_info()
account2.deposit(150).deposit(50).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()
