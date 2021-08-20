class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if amount >= self.balance:
            self.balance -= amount
            return True
        else:
            print("insufussent funds: charging a $5 fee")
            self.balance -= 5
            return False
        
    def display_account_info(self):
        print(self.balance)
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance =self.balance * self.int_rate
        return self
        
        
my_account1 = BankAccount()
my_account2 = BankAccount()

print (my_account1.deposit(100).deposit(200).deposit(40).withdraw(700).yield_interest().display_acount_info())


print (my_account2.deposit(200).deposit(60).withdraw(90).withdraw(30).withdraw(5).withdraw(50).display_acount_info().yield_interest())
