class User:
    def __init__(self,name, email):
        self.name = name
        self.email=email
        self.account_balance=0
        
    def make_deposit(self,amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance-=amount
    def display_user_balance(self):
        self.name, self.account_balance
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


mika = User("Mereilim Aitassova","ameekah93@hmail.com")
rassul=User("Rassul Aitassov", "rassul@gmail.com")
alim=User("Alim Hamza", "alim@gmail.com")

print(mika.name)
print(rassul.name)

mika.make_deposit(100)
mika.make_deposit(200)
rassul.make_deposit(50)
alim.make_deposit(100)

mika.make_withdrawal(200)
rassul.make_withdrawal(25)
alim.make_withdrawal(50)

mika.transfer_money(rassul,100)

print("User: "+ rassul.name + " Balance: "+str(rassul.account_balance))	# output: 300
print("User: "+ mika.name + " Balance: "+str(mika.account_balance))
print("User: "+ alim.name + " Balance: "+str(alim.account_balance))
