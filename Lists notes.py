#example
inv = []
inv = ["sword", "shield", "pots"]
print("you have", len(inv), "items")
chest = ["gold", "silver"]
inv += chest
print(inv)

empty = [] #list with no member, empty list
integers = [1, 2, 3] # list of integers
num_list = [1, 2.5, 3.7, 9] #list of numbers (integers and floating point)
letter_list = ['a', 'b', 'c'] # list of characters
mixed = ['a', 1, 'b', 3.5, 'zero'] # list of mixed value types
string_list = ['One', 'Two', 'Three'] # list of strings

y = [2, 4, 6]
z = [1, 2.0, 3, 4.8]
x = ["abc", "def"]
#formula = [value1, value2, etc]
sqrs = [0, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169,
        196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625]
print(sqrs)
#nested lists
L1 = [3,4,[5,6],7]
print(L1)
#inputting
l1 = list(input("Enter list elements: "))
print(l1)
#converting
t = ("w", "e", "r", "t", "y")
l2 = list(t)
print(l2)
#eval function
list1 = eval(input("Enter list to be added: "))
print("list you entered:",list1)
y = eval("5+8") #not only used for addition
print(y)
val1 = eval(input("Enter value: "))
print(val1, type(val1)) #stores result as int value
#You can use eval() to enter a list or tuple also. Use [ ] to enter lists' and () to enter tuple values
var1 = eval(input("Enter Value: "))
print (var1, type(var1))
#Enter Value: [1, 2, 3]  <class 'list'>
var1 = eval(input("Enter Value: "))
print (var1, type (var1))
#Enter Value: (2, 4, 6, 8)  <class 'tuple'>

#Accessing individual elements
vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels[0])
print(vowels[5])
print(vowels[-1])
print(vowels[-3])
#Replacing elements in a list
vowels[0] = 'A'
vowels[-4] = 'E'
print(vowels)

#For loops
#Format: for *item* in *list*:
L = ['P', 'y', 't', 'h', 'o', 'n']
for a in L:
    print(a)

L= ['q', 'w', 'e', 'r', 't', 'y']
length = len(L)
for a in range(length):
    print("At indexes", a, "and", (a - length), "element:", L[a])

a = [2, 3]
b = [2, 3]
c = ['2', '3']
d= [2.0, 3.0]
e = [2, 3, 4]
a == b
#True
a == c
#False

a > b
#False
d > a
#False
d == a
#True
a < e
#True

#Joining  lists
first1 = [1, 3, 5]
first2 = [6, 7, 8]
print(first1 + first2)

#Repeating + replicating lists
first1*3
print(first1)
#slicing lists
first =[10, 12, 14, 20, 22, 24, 30, 32, 34]
seq = first [3:-3]
print(seq)
#[20, 22, 24]
seq[1] = 28
print(seq)
#[20, 28, 24]