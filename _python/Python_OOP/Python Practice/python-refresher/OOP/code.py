
#converting age to months
# user_age = int(input("Enter your age"))
# months = user_age * 12
# print(f"Your age, {user_age}, is equal to {months} months.")


#list can Add,Remove, Edit
l = ["Bob", "Rolf", "Ann"]


print(l[0])
l[0]="Smith"
print(l[0])
l.append("Smith")
print(l)
l.remove("Smith") #['Rolf', 'Ann', 'Smith']
print(l)

#tuple can NOT modify,add,remove
t = ("Bob", "Rolf", "Ann")

print(t[2])


#set  no Bob x2 in the set
s = {"Bob", "Rolf", "Ann"} 

s.add("Smith")
print(s)  #{'Bob', 'Rolf', 'Ann', 'Smith'}

s.add("Smith")
print(s)  #{'Ann', 'Smith', 'Bob', 'Rolf'}






