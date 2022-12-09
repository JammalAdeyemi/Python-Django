# Write a program to check if a a year is a leap year or not
year = int(input("What year do you want to start with? "))
no_years = int(input("How many years do you want to check? "))

# Loop through the years
for i in range(year, year + no_years):
    # Check if the current year is a leap year
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(f"{i} is a leap year")
    else:
        print(f"{i} isn't a leap year")

