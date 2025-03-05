# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

counter = 0
even = []

while counter < 10:
    counter += 1
    nums = float(input("Enter 10 numbers: "))

    if nums % 2 == 0:
        even.append(nums)

print(len(even))

