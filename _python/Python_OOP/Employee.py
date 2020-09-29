class Employee:
    def __init__(self, name, lastname, pay):
        self.name=name
        self.lastname=lastname
        self.email=name + '.'+lastname+'@gmail.com'
        self.pay=pay

    def fullname(self):
        return '{} {}'.format(self.name, self.lastname)



emp1=Employee("Mika", "Aitassova",50000 )
emp2=Employee("Alim", "Hamza",60000)


print(emp1.email, emp1.pay)
print(emp2.email)

print(emp1.fullname())
print(emp2.fullname())

Employee.fullname(emp1)


