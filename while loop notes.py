#Example 1 - While Loops
#Print all the multiples of 5 up to a limit set by the user.
user_limit = int(input('Enter an integer limit on the multiples of 5: '))

multiples = 5
while multiples < user_limit:
    print(multiples)
    multiples = multiples + 5
print()

#Example 2
#Print all the even numbers in a range given by the user.
start_value = int(input('Enter an integer start value: '))
end_value = int(input('Enter an integer end value: '))

while start_value <= end_value:
    if start_value % 2 == 0:
        print(start_value)
    start_value = start_value + 1
print()

#Example 3
#Add all the numbers a user enters until they enter a negative number.
#Print the total at the end.

user_number = int(input('Enter an integer number: '))
running_total = 0
if user_number >= 0:
    while user_number > 0:
        running_total = running_total + user_number
        user_number = int(input('Enter an integer number: '))
    else:
        print('The total of the positive numbers entered was: ',running_total)
else:
    print('The total of the positive numbers entered was: ',running_total)