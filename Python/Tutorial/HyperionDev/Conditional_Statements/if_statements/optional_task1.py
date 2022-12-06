# This program should test whether a number is odd or even.

user = int(input("Input a integer: "))

if user % 2 == 0:
    print(f"\n{user} is a even number.")
else:
    print(f"\n{user} is an odd number.")