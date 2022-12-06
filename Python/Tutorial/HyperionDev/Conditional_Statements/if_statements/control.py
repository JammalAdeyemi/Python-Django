# This program will be used to test if the user is 18 or older and allowed entry into a party.

age = int(input("Kindly input your age: "))

if age >= 18:
    print("You are old enough!")
elif age > 16 or age < 18:
    print("Almost there")
else:
    print("You’re just too young!")