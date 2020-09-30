t = (5 , 11)
x, y = t
print(x, y)



student_attend = {"Rolf":96, "Bob":86, "Ann":75}

# for student, attend in student_attend.items():
#     print(f"{student} : {attend}")

# attend_values = student_attend.values()
# print(sum(attend_values)/len(attend_values))


print(list(student_attend.items()))


for t in student_attend.items():  #tupling each student and its value
    print(t)



for student, attend in student_attend.items():
    print(f"{student} : {attend}")