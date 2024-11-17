num = 20131452
total = 0
mul = 2
while num > 0:
    digit = num % 10 
    num = num // 10
    total += digit*mul
    mul += 1  # mul = mul + 1
print(total)
checksum = total%11
checksum = 11 - checksum
print(checksum)