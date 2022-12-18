# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "Lion" # NameError: name 'Lion' is not defined
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth" # SyntaxError: Add the f-string

print (full_spec) # SyntaxError: Missing parentheses in call to 'print'

