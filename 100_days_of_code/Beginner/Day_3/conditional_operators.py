print("Welcome to the rollercoster!")
height = int(input("Input your height in cm: "))
bill = float(0)
if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("Input your age: "))
    if age < 12:
        bill = 5
        print("Child ticket is £5.0")
    elif age <= 18:
        bill = 7.50
        print("Adult tickets are £7.5")
    elif age >= 45 and age <=55:
        bill = 0
        print("Have a free ride on us!")
    else:
        bill = 15
        print("Teenage tickets are £15")
    
    photos = input("Do you want a photo taken? Y or N: ")
    if photos == "Y":
        # Add £3 to their bill
        bill += 3
    print(f"Your final bill is £{bill}")
else:
    print("sorry, you have tp grow taller before you can ride. ") 