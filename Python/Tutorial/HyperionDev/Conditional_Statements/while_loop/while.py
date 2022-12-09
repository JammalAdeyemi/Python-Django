# Write a program that always asks the user to enter a number

# initialize a variable to store the sum of the numbers entered by the user
total = 0
# initialize a variable to store the number of numbers entered by the user
count = 0

# prompt the user to enter a number
while True:
    user = input("Enter a number (or -1 to exit the loop): ")
    if user == "-1":
        # code stopes when user enter -1
        break
    else:
        total += float(user)
        count += 1

# calculate the average of the numbers entered by the user
average = total / count

# print the average
print(f"Average: {average}")
