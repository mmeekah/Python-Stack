class BankAccount:
    def __init__(self, balance, interest):
        self.balance=balance
        self.interest=interest


class User:
    def __init__(self, name, email):
        self.name=name 
        self.email=email
        self.account=BankAccount(interest=0.02, balance=0)
        # self.account2=BankAccount(interest=0.02, balance=0)


    def deposit(self,amount):
        self.account.balance += amount
        print(" {} deposited - ${}".format(self.name,self.account.balance))
        return self

    def withdrawal(self,amount):
        if self.account.balance < amount:
            print('insufficient funds: charging $30')
            self.account.balance -=(amount +30)
            print("now  balance is ${}".format(self.account.balance))
        
        else:
            self.account.balance -= amount
            print(" {} withdrawed - ${}".format(self.name,self.account.balance))
            return self

    def display_account_info(self):
        print("{}s balance is ${}".format(self.name, self.account.balance))
        return self
    
    def transfer_money(self, amount, other_user):
        self.account.balance -=amount
        print("Transferring {} ${}".format(other_user.name, amount))
        other_user.account.balance +=amount
        print("${} transferred to {}".format(amount, other_user.name))
        # print("Total balance remained {}.".format(self.account.balance))
        return self

    def yield_interest(self):
        if self.account.balance >=0:
            self.account.balance *=account.interest
            print("Interest rate applied, and balance is ${}".format(self.account.balance))
        else:
            print("{}'s balance is negative, {}".format(self.name, self.account.balance)


    
mika = User("Mika", "ameekah@hmail.com")
# rassul = User("Rassul", "rassul@gmail.com")

mika.deposit(100).withdrawal(10).transfer_money(rassul,10).display_account_info().yield_interest()
