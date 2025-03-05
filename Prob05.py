# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if num2 == 0:
    print("Undefined")
else:
    rem = num1 % num2
    print(rem)