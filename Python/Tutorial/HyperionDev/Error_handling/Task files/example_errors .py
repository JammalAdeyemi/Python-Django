# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.
 
name = "Tim"
surname = " Jones"
age = 21
 
fullMessage = name + surname + " is " + str(age) + " years old"  # TypeError: can only concatenate str (not "int") to str
 
print(fullMessage)  # SyntaxError: Missing parentheses in call to 'print'

