class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
    def make_account(self):
        self.accounts.append(BankAccount(0, 0.05))
        return self

class BankAccount:
    def __init__(self, balance, int_rate):
        self.int_rate = 0.05
        self.balance = 0
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
        self.balance += (self.balance * self.int_rate * 1)
        return self
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self

jerome = User('Jerome', 'jerome.j.johnson@outlook.com')
james = User('James', 'jeromejohnson46@yahoo.com')
sarah = User('Sarah', 'sarah.d@gmail.com')

jerome.make_account().accounts[0].deposit(500).deposit(50).deposit(150).withdraw(250).yield_interest().display_account_info()
jerome.make_account().accounts[1].deposit(1000).yield_interest().display_account_info()
james.make_account().accounts[0].deposit(150).deposit(50).withdraw(25).withdraw(25).withdraw(25).withdraw(25).display_account_info().yield_interest().display_account_info()


