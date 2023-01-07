# You will need to import the math module and use its built-in functions tocomplete this task.
import math
# Write a program that starts by asking the user to input 10 floats (these can be a combination of whole numbers and decimals). Store these numbers in a list.
numbers = []
user = input('Enter 10 floats: ')
numbers.append(user)

# Find the total of all the numbers and print the result.
total = sum(numbers)
print(f'The total sum of all float numbers inputted is {total}')

# Find the index of the maximum and print the result.
max_index = numbers.index(max(numbers))
print(f'The index of the maximum number is {max_index}')

# Find the index of the minimum and print the result.
min_index = numbers.index(min(numbers))
print(f'The index of the minimum number is {min_index}')

# Calculate the average of the numbers and round off to 2 decimal places.
average = total / len(numbers)
print(f'The average of all the numbers is {round(average, 2)}')

# Find the median number and print the result.
median = numbers[len(numbers) // 2]
print(f'The median number is {median}')
