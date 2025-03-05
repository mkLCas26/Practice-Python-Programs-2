# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

num1 = float(input("Enter 10 numbers: "))
remNum = 0
counter = 0

while counter < 9:
    counter += 1
    nums = float(input("Enter 10 numbers: "))
    remNum += nums

diff = num1 - remNum
print(diff)
    