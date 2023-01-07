# Write a Python program called counting.py to count the number of times a character occurs (character frequency) in a string.

user = input('Enter a string: ')

# Create a dictionary called charCount, where the KEYS are the characters in the string, and the VALUE for each key is the number of times that character occurs in the string.
charCount = {}

# Store each letter followed by the number of occurrences in a dictionary and print it out.
for char in user:
    if char in charCount:
        charCount[char] += 1
    else:
        charCount[char] = 1
print(charCount)
