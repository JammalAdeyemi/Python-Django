# Write a Python program called John.py that takes in a user’s input as a string.
incorrect_strings = []

# While the string is not “John”, add every string entered to a list until “John” is entered. This program basically stores all incorrectly entered strings 
# in a list where “John” is the only correct string.
while True:
    string = input("Enter a user name: ").lower()
    if string == "john":
        break
    else:
        incorrect_strings.append(string)
# Print out the list of incorrect names.
print(incorrect_strings)
# HINT: When testing your While loop, you can make use of .upper() or .lower() to eliminate case sensitivity.
