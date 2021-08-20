from banlaccount
class User:		
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


lana = User("lana")
lana.make_deposit(1000)
lana.make_deposit(9720)
lana.make_deposit(100)
lana.make_withdrawal(50)
lana.display_user_balance()

nizam = User("nizam")
nizam.make_deposit(720)
nizam.make_deposit(20)
nizam.make_withdrawal(720)
nizam.make_withdrawal(700)
nizam.display_user_balance()

lana = User("Hadeel")
lana.make_deposit(1000)
lana.make_deposit(9720)
lana.make_withdrawal(79)
lana.make_withdrawal(50)
lana.display_user_balance()




