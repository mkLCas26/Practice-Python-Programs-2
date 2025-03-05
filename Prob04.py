# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if num2 == 0:
    print("Undefined")
else:
    quo = num1 / num2
    print(int(quo))