
class BankAccount:
    
        def __init__ (self, int_rate =0.03, balance =0): 
            self.int_rate = int_rate
            self.balance=balance
        def deposit(self, amount):
            self.balance += amount
            return self           
        def withdraw(self, amount):
            self.balance -=amount
            if self.balance<0:
                print("Insufficient funds: Charging $30")
                self.balance=-30
            return self
        def display_account_info(self):
            print("Balance: {}".format(self.balance))
            return self.balance
        def yield_interest(self):
            self.balance *= 1 + self.int_rate
            return self
		


acc1=BankAccount(0.05, 200)
acc1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
acc2=BankAccount()
acc2.deposit(100).deposit(200).deposit(100).withdraw(100).yield_interest().display_account_info()
