#1
x = int(input('How many days of work for x? '))
y = int(input('How many days of work for y? '))
z = int(input('How many days of work for z? '))
xyz = x * y * z
xy = x * y
yz = y * z
xz = x *z
formula = xyz/(xy + yz + xz)
print(formula)

#2
num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))
add = num1 + num2
subtract = num1 - num2
divide = num1/num2
multiply = num1*num2
exponent = num1**num2
modulus = num1%num2
floor_divison = num1//num2
print(add, subtract, divide, multiply, exponent, modulus, floor_divison)

#3
print('Question 3')
a=1
b=2
c=a #c=1
a=b #a=2
b=c #b=1
print(a,b)

#4
print('Question 4')
m=1
n=2
m,n=n,m
print(m,n)

#5
number1 = float(input('Enter the first number to find the average of: '))
number2 = float(input('Enter the second number to find the average of: '))
number3 = float(input('Enter the third number to find the average of: '))
process = number1 + number2 + number3
average = process/3
print(average)

#6
PI = 3.14
r = float(input('What is the radius? '))
volume = 4/3*PI*r**3
print(volume)

#7
name = input('What is your name? ')
age = int(input('What is your age? '))
old = 100-age
year = 2024+old
print(year)

#8
mass = float(input('Enter a mass: '))
speed = 3*10**8
formula = mass*speed**2
print('The energy of this mass is:',formula)

#9
print('Name Of School')
name = input('Enter student name: ')
student_class = input('Enter your class: ')
address = input('Enter your address: ')
address2 = input('Enter a second address: ')
city = input('Enter your city: ')
contact = input('Enter a contact number: ')
roll = input('Enter your roll number: ')
section = input('Enter your section: ')
pin = (input('Enter your pin code: '))
print('Student Name:',name,'\tRoll No. ', roll)
print('Class:',student_class, '\tSection:', section)
print('Address:',address, '\n\t',address2)
print('City:',city, '\tPin Code:',pin)
print('Parents/Guardians Contact No:', contact)