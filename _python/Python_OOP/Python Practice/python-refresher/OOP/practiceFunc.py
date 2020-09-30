student ={ "name": "Mika", "school": "CS", "grades": (89,99,100)}


def avg_grade(data):
    grades = data["grades"]
    return sum(grades)/len(grades)




def avg_grade_all_students(students_list):
    total=0
    count =0
    for student in students_list:
        total=total+sum(student["grades"])
        count = count+len(student["grades"])
        
    return total/count
