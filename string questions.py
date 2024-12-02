s1 = 'must'
s2 = 'try'
n1 = 10
n2 = 3
print(s1 + s2)
print(s2 * n2)
print(s1 + n1)
print(s2 * s1)

#Line 7 is a string added by a integer which you cannot do
#Line 8 is a string multipled by a string which you cannot do

string = (input('Enter a string: '))
count = 3
while True:
       if string[0] == 'a':
           string = string[2:]
       elif string[-1] == 'b':
           string = string [:2]
       else:
           count += 1
       break
print(string)
print(count)

#5
string = input('Enter a string: ')
length = len(string)
a = 0
end = length
string2 =''
while a < length:
    if a == 0:
        string2 += string[0].upper()
        a += 1
    elif(string[a] == ' ' and string[a+1] !=''):
        string2 += string[a]
        string2 += string[a+1].upper()
        a += 2
    else:
        string2 += string[a]
        a += 1
print("Original String:", string)
print("Capitalized words String: ", string2)

#6
string = input('Enter a string: ')
length = len(string)
mid = length//2
rev = -1
for a in range(mid):
    if string[a] == string[rev]:
        a += 1
        rev -= 1
    else:
        print(string, 'is not a palindrome')
        break
else:
        print(string, 'is a palindrome')

#7
string = input('Enter a string: ')
length = len(string)
maxlength = 0
maxsub = ''
sub = ''
lensub = 0
for a in range(length):
    if string[a] in 'aeiou' or string[a] in 'AEIOU':
        if lensub > maxlength:
            maxsub = sub
            maxlength = lensub
            sub = ''
            lensub = 0
    else:
        sub += string[a]
        lensub = len(sub)
    a += 1
    print('Maximum length consonant substring is: ', maxsub, end = '')
    print('with', maxlength, 'characters')
#8
string = input('Enter a string: ')
length = len(string)
print('Original string: ', string)
string2 = ' '
for a in range(0, length, 2):
    string2 += string[a]
    if a < (length-1):
        string2 += string[a + 1].upper()
print('Alternatively capitalized string:', string2)

#9
email = input('Enter your email: ')
domain = '@edupillar.com'
lendom = len(domain)
lenmail = len(email)
stringStartPositionValue = lendom-lenmail
sub = email[stringStartPositionValue:]
if sub == domain: #sub = email without domain
    if lendom != lenmail: #lenght of email has to be different to the lenght of the domain
        print('It is a valid email')
    else:
            print('You have entered an invalid email which only contains the domain')
else:
        print('This email is either not valid or belongs to a different domain')
            