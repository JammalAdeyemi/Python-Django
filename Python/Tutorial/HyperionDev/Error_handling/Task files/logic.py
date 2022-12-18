#  Write a program that displays a logical error (be as creative as possible!).

# This program is designed to calculate the factorial of a number
number = 5
factorial = 1

# Calculate the factorial of the number
for i in range(1, number):  # Logical error: the range should go up to number + 1, not number
    factorial *= i

print(f"The factorial of {number} is {factorial}")
