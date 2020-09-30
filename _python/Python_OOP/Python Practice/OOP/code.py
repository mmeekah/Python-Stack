class Student:
    def __init__(self, name, grade):
        self.name =name
        self.grades = grade



    def average_grade(self):
        return sum(self.grades)/len(self.grades)


student = Student("Bob", (100, 100, 95, 93))
print(student.name)
print(student.grades)
print(Student.average_grade(student)) #same as down

print(student.average_grade())