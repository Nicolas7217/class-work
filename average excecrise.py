#1
user_number = input('Enter an integer number: ')
running_total = 0
counter = 0
while user_number !='' :
    user_number = int(user_number)
    running_total = running_total + user_number
    counter = counter + 1
    user_number = input('Enter an integer number: ')
else:
     print('The total of the positive numbers entered was: ',running_total/counter)
     
#2
user_number = int(input('Enter an integer number: '))
running_total = 0
counter = 0
while user_number >= 0 :
    user_number = int(user_number)
    running_total = running_total + user_number
    counter = counter + 1
    user_number = int(input('Enter an integer number: '))
else:
     print('The total of the positive numbers entered was: ',running_total/counter)
     
#3
user_number = int(input('Enter the test grades: '))
running_total = 0
counter = 0
while user_number >= -1 :
    user_number = int(user_number)
    running_total = running_total + user_number
    counter = counter + 1
    user_number = int(input('Enter the test grades: '))
else:
     print('The average of the grades is: ',running_total/counter)
if user_number >= 90:
         print('Congratulations, You got an A!')
elif user_number >= 80 and user_number <= 89:
         print('Good, You got a B')
elif user_number >= 70 and user_number <= 79:
         print('You got a C')
elif user_number >= 60 and user_number <= 69:
         print('You got a D, do you want to work at McDonalds?')
elif user_number <= 59:
         print('An F, goodluck showing this to your parents!')
         
#4    
num1 = int(input('Enter a number: '))
while num1 >= 0:
    print(num1)
    num1 = num1 - 1

#5
num1 = int(input('Enter a number: '))
num2 = 0

while num2 <= num1:
    if num2%2 == 0:
        print(num2)
    num2 = num2 + 1