#1
for i in range (1,10):
    print(i)
#2
    
for a in range (10,-1,-1):
    print(a)
#3
string = '#'
for t in range (1,7,1):
    print(string*t)
#4
rows = int(input('How many rows are there? '))
columns = int(input('How many columns are there? '))
#tbc

#5
num1 = 0
num2 = 0
for i in range (0,10,1):
    num1 += 1
    num2 += 1
    value = num1*num2
    print(num1, 'x', num2, '=', value)
#6
for i in range (1,100):
    if i%2 == 0:
        print(i)
#7
for i in range (1,100):
    if i%2 == 1:
        print(i)