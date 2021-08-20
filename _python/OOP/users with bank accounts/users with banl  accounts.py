from bankaccount import BankAccount

class User:		
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()
        
    def deposit(self, amount):
        self.account.deposit(amount)
        
    def make_withdrawal(self, amount):
        return self.account.withdraw(amount)
        
    def display_user_balance(self):
        print(f"{self.name} balance is:", end = " ")
        self.account.display_account_info()
        
    def transfer_money(self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.deposit(amount)
            return True
        return False
