age = 24
print("My age is " + str(age) + " years")
# String replacement
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4} and {5}"
        .format(31, "Jan", "Mar", "May", "Jul", "Aug"))
print()

# String Formatting
for i in range(1,12):
        print("No. {0:2} squared is {1:2} and cubed is {2:3}".format(i, i**2, i**3))