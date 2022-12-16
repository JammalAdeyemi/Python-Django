age = 24
print("My age is " + str(age) + " years")
# String replacement
print("'String replacement'")
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4} and {5}"
        .format(31, "Jan", "Mar", "May", "Jul", "Aug"))
print("'String Formatting'")

# String Formatting
for i in range(1,12):
        print("No. {0:2} squared is {1:2} and cubed is {2:3}".format(i, i**2, i**3))

# f-string
age = 24
name = "Jammal"
age_in_words = "2 years"
print("'f-string'")
print(name + f" is {age} years old")
print(f"Pi is approcimately {22 / 7:12.50f}")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")