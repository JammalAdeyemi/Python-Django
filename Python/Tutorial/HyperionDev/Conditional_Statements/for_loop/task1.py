#  This program needs to make use of for loops in order to display the times tables for any number.

# Ask the user for an input
user = int(input("Enter a number: "))

# Loop through the numbers from 1 to 12
for i in range(1, 13):
    # get the product through the loop
    product = user * i
    # print out the multiplication table
    print(f"{user} * {i} = {product}")