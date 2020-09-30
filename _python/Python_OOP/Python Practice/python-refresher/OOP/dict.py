student_attend = {"Rolf":96, "Bob":86, "Ann":75}

# for student in student_attend:
#     print(f"{student}: {student_attend[student]}")


for student, attend in student_attend.items():
    print(f"{student} : {attend}")

attend_values = student_attend.values()
print(sum(attend_values)/len(attend_values))