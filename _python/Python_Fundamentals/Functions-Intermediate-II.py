
#Update Values in Dictionaries and Lists
#1
x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)

#2
# students["last_name"] = 2018
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# for i in students:
#    for j in i:
#        if i.get(j)=='Jordan':
#            i.update({j: 'Bryant'})

students[0] = {'first_name': 'Michael', 'last_name': 'Bryant'}
print(students
print(students)

#3

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer']=['Andres', 'Ronaldo', 'Rooney']
print(sports_directory)

#4
z = [ {'x': 10, 'y': 20} ]
z = [ {'x': 10, 'y': 30} ]
print(z)

#Iterate Through a List of Dictionaries


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDict(dict):
    for student in students:
        for key, val in student.items():
            print(key, " - ", val)

iterateDict(students)

# Get Values From a List of Dictionaries


def iterateDict2(lookup, dict):
    for student in students:
        print(student[lookup])

iterateDict2('first_name', students)


#Iterate Through a Dictionary with List Values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDojoInfo(list):
    for key in dojo:
        print(str(len(dojo[key]))+ " "+ key.upper())
        for val in dojo[key]:
            print(val)

printDojoInfo(dojo)