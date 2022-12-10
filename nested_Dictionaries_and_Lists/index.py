# 1)

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30
print(x)
print(students)
print(sports_directory)
print(z)

print("---------------")
# 2)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary(students):
    for student in students:
        namestring = "first_name - " + student["first_name"] + ", last_name - " + student["last_name"]
        print(namestring)

iterateDictionary(students) 
print("---------------")
# 3)

def iterateDictionary2(key_name, students):
    for student in students:
        print(student[key_name])

iterateDictionary2("last_name", students)
print("---------------")
# 4)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print(len(dojo["locations"]), " LOCATIONS")
    for local in dojo["locations"]:
        print(local)

    print("")

    print(len(dojo["instructors"]), " Instructors")
    for teacher in dojo["instructors"]:
        print(teacher)
    
printInfo(dojo)
