if True: #or if False
    print("inside if coz if condition is true")
else:
    print("Inside else coz if condition is false")
if not True: #or if False
    print("inside if coz if condition is true")
else:
    print("Inside else coz if condition is false")

for i in range(1,6,2): #(include 1, exclude 6, add or step size of 2)
    print(i, end=" ")
print(list(range(2,15,3)))

for i in range(1,7):
    print("*" * i)

arr = [1,2,3,4,5]
brr = arr
brr[0]=10
print(arr)

a=10
b=a
b=15
print(a)

a = "pakistan zindabad"
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())

#List

student = ["Khizra", "03472033493", "Shah Faisal Colony", "Niaz Ali"] #in list you have to remember what is stated in first address 2nd and so on
print(student)
student[0]='Khizra Ali'
print(student)

#Dictionary

student = {# in dictionary you can give key like name, no etc
    'Name':'Khizra',
    'Mobile No':'03472033493',
    'Address':'Shah Faisal Colony',
    'Father Name': 'Niaz Ali'
}
print(student)
student['Name']='Khizra Ali'
print(student)
#del student['Address']
print(student.pop('Address'))
print(student)

students = []
for i in range(3):
    student={}
    student['name']=input('your name: ')
    student['Cell no']=input('your number: ')
    student['Father name']=input('your fathers name: ')
    students.append(student)
print('Currently enrolled students: ', len(students))
for student in students:
    print('student')
    print(student)
    if student['name'].lower()=='inam':
        print('yes inam is our student')
    else:
        print('sorry')

student = {
    'Name':'Khizra',
    'Mobile No':'03472033493',
    'Address':'Shah Faisal Colony',
    'Father Name': 'Niaz Ali'
}

for k,v in students.name:
    print(v)
