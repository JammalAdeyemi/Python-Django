# This program will be used to validate that a user inputs at least two names when asked to enter their full name.

name = input("Input your fullname: ")

if len(name) == 0:
	print ("You haven’t entered anything. Please enter your full name.")

elif len(name) < 4:
	print ("You have entered less than 4 characters. Please make sure that youhave entered your name and surname.")

elif len(name) > 25:
	print ("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

else:
    print("Thank you for entering your name.")

print(name)