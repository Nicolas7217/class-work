'''
#1
pn = input('Enter your phone number: ')
if pn[3] == '-' and pn[7] == '-':
    if pn[0:2].isdigit() and pn[4:6].isdigit() and pn[8-11].isdigit():
        print('This is a valid phone number')
else:
    print('This phone number is invalid')
    
#2
string = input('Enter a string: ')
total = 0
digits = False
for character in string:
    if character.isdigit():
        total += int(character)
        print('The digits in this string are:', character)
        digits = True
print('Original string:', string)
print('The sum of the digits in this string are:', total)
if not digits:
   print('has no digits')
   
#3
sentence = input('Enter a sentence: ')
print('original sentence:', sentence)
length = len(sentence)
print('there are',length,'letters in this sentence')
words = sentence.split()
count = 0
for word in words:
    count += 1
    print(count)
#use .isalnum() to check each letter and add to a counter then divide
counter = 0
for letter in sentence:
    if letter.isalnum():
        counter += 1
percentage = counter / length
print('the percentage of character which are alphanumeric is',percentage,'%')
'''
#4
sentence1 = input('Enter a sentence or enter q to quit')
