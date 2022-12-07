user = int(input("Enter an integer: "))

if (user % 2 == 0) and (user % 5 == 0):
    print(f"{user} is divisible by 2 & 5.")

elif (user % 2 == 0) or (user % 5 == 0):
    print(f"{user} is divisible by 2 / 5.")

else: # (user % 2 != 0) or (user % 5 != 0)
    print(f"{user} is not divisible by 2 / 5.")