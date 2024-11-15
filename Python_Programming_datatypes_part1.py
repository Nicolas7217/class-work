#1
Mon_temp = float(input('What was the temeprature on Monday? '))
Tue_temp = float(input('What was the temeprature on Tuesday? '))
Wed_temp = float(input('What was the temeprature on Wednesday? '))
Thu_temp = float(input('What was the temeprature on Thursday? '))
Fri_temp = float(input('What was the temeprature on Friday? '))
Sat_temp = float(input('What was the temeprature on Saturday? '))
Sun_temp = float(input('What was the temeprature on Sunday? '))
answer = (Mon_temp + Tue_temp + Wed_temp + Thu_temp + Fri_temp + Sat_temp + Sun_temp)
average = (answer/7)
print(average)

#2
x = float(input('What is x? '))
y = float(input('What is y? '))
z = float(input('What is z? '))
PI = 3.14
xyz = (4*x**4 + 3*y**3 + 9*z + 6*PI)
print(xyz)

#3
seconds = int(input('How many seconds are there? '))
minutes = seconds//60
seconds2 = seconds%60
print(minutes, seconds2)

#4
hour = int(input('Enter an hour between 1 and 12: '))
ahead = int(input('How many hours ahead would you like to know? '))
time = hour + ahead
print('In', hour, 'hours it will be', time%12, 'oclock')

#5
num = int(input('Enter a 3 digit number: '))
num2 = num%10 #=3
num3 = num//10 #=12
num4 = num3%10 #=2
num5 = num3//10 #=1
print(num2, num4, num5, sep="")

#6
day = int(input('Enter a day: '))
month = int(input('Enter a month '))
month2 = month*30
days = month2 + day

print("this is day", days, 'of the current year')
