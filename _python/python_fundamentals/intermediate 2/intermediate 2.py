# 1
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
print(x)

students[0]['last_name'] = 'Braynt'
print(students)


sports_directory['soccer'][0] = 'andres'
print(sports_directory)

z[0]['y'] = 30
print(z)
print('-' * 30)


# 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for student in students:
        print(f"first name - {student['first_name']}, last name - {student['last_name']}")
iterateDictionary(students)
print('_' * 30)


# 3 
def iterateDictionary2(key_name, other_list):
    for i in other_list:
        print(i[key_name])
iterateDictionary2('first_name', students)
print('_' * 30)

# 4

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key, values in dojo.items():
        print(f"{len(values)} {key}")
        for value in values:
            print(value)
printInfo(dojo)




