# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

noZero = []

for num in range(0, 100):
    if num % 10 != 0 and num % 5 != 0:                   
        noZero.append(num)

print(noZero)