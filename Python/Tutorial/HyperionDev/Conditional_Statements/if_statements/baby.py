# This program will be used to test if the user is 18 or older and allowed entry into a party.

user = int(input("Kindly input your birth year: "))
current_age = 2022 - user
if current_age > 18:
    print("Congrats you are old enough")
else:
    print("Sorry you are not eligible")