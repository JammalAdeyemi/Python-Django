# Write a program that asks the user to enter a number.
user = int(input("Input a number: "))
i = 1
# the program prints out all the even numbers from 1 up to (and possibly including) the number given by the user.
while i <= user:
    # Checking for even number
    if i % 2 == 0:
        print(i, end = " ")
    i += 1
