# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program")  # SyntaxError: Missing parentheses in call to 'print'
print("\n")

ageStr = "24 years old"  # SyntaxError: can't assign to operator
age = int(ageStr[:2])  # ValueError: invalid literal for int() with base 10: '24 years old'
print("I'm " + str(age) + " years old.")  # TypeError: can only concatenate str (not "int") to str
three = "3"

answerYears = age + int(three)  # TypeError: can only concatenate str (not "int") to str

print("The total number of years: " + str(answerYears))  # TypeError: can only concatenate str (not "int") to str
answerMonths = answerYears * 12 + 6
print("In " + str(answerYears) + " years and 6 months, I'll be " + str(answerMonths) + " months old")  # TypeError: can only concatenate str (not "int") to str

#HINT, 330 months is the correct answer











