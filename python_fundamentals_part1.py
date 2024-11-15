#1
pi = 3.14
radius = float(input('What is the radius of a circle? '))
area = pi*radius*radius
print(area)

#2
cm = int(input('What is your height in centimeters? '))
height_inches = cm / 2.54
height_feet = height_inches / 12
print(('Your height in inches is'), height_inches, ('your height in feet is'), height_feet)

#3
n = float(input('Enter a number: '))
a = n**2
b = n**3
c = n**4
print(a)
print(b)
print(c)

#4
base = float(input('Enter the base: '))
height = float(input('Enter the height '))
print('area:',base/2*height)

#5
name = input('Enter your name: ')
clas = input('Enter your class: ')
age = input('Enter your age: ')
print(name, clas, age)
print(name,'\n',clas,'\n',age)

#6
num = int(input('Enter a number: '))
num2 = num + 1
num3 = num + 2
print(num, num2, num3, sep='')

#7
num1 = input('Enter a number')
num1 = float(num1)
num2 = input('Enter a number')
num2 = float(num2)
num3 = input('Enter a number')
num3 = float(num3)
print(num1, num2, num3)
num1 = num1 + num2
num2 = num2 + num3
print(num1, num2, num3)
