friends = ["Rolf", "Jen", "Bob", "Ann"]


for friend in range(4):
    print(f"{friend} is my friend. ")


grades = [35, 67, 98, 100, 100]
total = sum(grades)
print(total)
amount = len(grades)

for grade in grades:
    total = total + grade
print(total / amount)


