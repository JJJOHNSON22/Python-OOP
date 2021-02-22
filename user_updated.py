class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):    
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        if (amount < self.account_balance):
            self.account_balance -= amount
            return self
        else:
            print('Insufficient Funds')
            return self
            
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.account_balance}')
        return self
        
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f'{self.name} has transfered money to {other_user.name}')
        self.display_user_balance()
        other_user.display_user_balance()
        return self

jerome = User('Jerome', 'jerome.j.johnson@outlook.com')
james = User('James', 'jeromejohnson46@yahoo.com')
sarah = User('Sarah', 'sarah.d@gmail.com')

jerome.make_deposit(100).make_deposit(200).make_deposit(500).make_withdrawl(100).display_user_balance().transfer_money(sarah,100)
james.make_deposit(50).make_deposit(500).make_withdrawl(150).make_withdrawl(50).display_user_balance()
sarah.make_deposit(900).make_withdrawl(100).make_withdrawl(200).make_withdrawl(50).display_user_balance()


