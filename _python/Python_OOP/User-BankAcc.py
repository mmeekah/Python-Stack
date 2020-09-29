class BankAccount:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest=0.02, balance=0)
        self.account1 = BankAccount(interest=0.02, balance=0)	# added this line

    def deposit(self,amount):
        self.account.balance += amount
        print(self.name, 'just deposit $',amount )
        print('now',self.name, 'with balance of $', self.account.balance,"\n","*"*30)
        return self
    
    def withdrawal(self,amount):
        if amount > self.account.balance:
            print(self.name, 'just withdraw $',amount )
            print('infufficient funds: charging a $5 fee')
            self.account.balance-= 5
            print('now',self.name, 'with balance of $', self.account.balance,"\n","*"*30)
            return self
        else: 
            self.account.balance -= amount
            print(self.name, 'just withdraw $',amount )
            print('Account',self.name, ': balance $', self.account.balance,"\n","*"*30)
            return self

    def display_account_info(self):
        print(self.name, ' balance is $', self.account.balance,"\n","*"*30)
        return self

    def transfer_money(self,other_user,amount):
        print('previous', self.name, 'with balance of $', self.account.balance)
        print('previous', other_user.name, 'with balance of $', other_user.account.balance)
        self.account.balance -= amount
        other_user.account.balance += amount
        print(self.name,'transfer $',amount,'to',other_user.name)
        print('now',self.name, 'with balance of $', self.account.balance)
        print('now',other_user.name, 'with balance of $', other_user.account.balance,"\n","*"*30)
        return self

    def yield_interest(self):
        if self.account.balance>=0:
            self.account.balance= self.account.balance*self.account.interest
            print('after interest rate, now',self.name, ' balance is $', self.account.balance,"\n","*"*30)
            return self
        else:
            print(self.name, 'is negative - balance - $',self.account.balance ,"\n","*"*30)
            return self



mika = User("Mereilim Aitassova","ameekah93@hmail.com")
rassul=User("Rassul Aitassov", "rassul@gmail.com")
alim=User("Alim Hamza", "alim@gmail.com")


mika.deposit(5).deposit(1000).deposit(500).withdrawal(590).yield_interest()
rassul.deposit(50).deposit(60).withdrawal(1000).withdrawal(1000).withdrawal(100000).withdrawal(1000000).yield_interest()