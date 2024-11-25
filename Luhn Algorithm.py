#Starting from the rightmost digit, double the value of every second unit

num1 = int(input('Enter an account number: '))
counter = 0
total = 0
while num1 > 0:
      counter = counter + 1
      num2 = num1 % 10
      num1 = num1 // 10
      print(num1, num2)
      if counter%2 ==0:#%2 == 0 for an even number.  %2 == 1 for an odd number
          num3 = num2*2
          if num3 <= 9:
              total = total + num3
          else:
              total = num3%10 + num3//10 + total
      else:
          total = num2 + total
      print(total)
           