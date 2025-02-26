#3
theStr = "This is a test"
inputStr = input('Enter integer: ')
inputInt = int(inputStr)
testStr = theStr
while inputInt >= 0:
    testStr = testStr[1:-1]
    inputInt = inputInt -1
testBool = "t" in testStr
print(theStr)
print(testStr)
print(inputInt)
print(testBool)

#4
testStr = "abcdefghi"
inputStr = input ("Enter integer:")
inputlnt = int(inputStr)
count = 2
newStr = ''
while count <= inputlnt:
    newStr = newStr + testStr[0: count]
    testStr = testStr[2:]
    count = count + 1
print (newStr)
print (testStr)
print (count)
print (inputlnt)

#5
inputStr = input("Give me a string: ")
bigInt = 0
littleInt = 0
otherInt = 0
for ele in inputStr:
    if ele >= 'a' and ele <= 'm':
        littleInt = littleInt + 1
    elif ele > 'm' and ele <= 'z':
        biglnt = biglnt + 1
else:
    otherInt = otherInt + 1
print (bigInt)
print (littleInt)
print (otherInt)
print (inputStr.isdigit())