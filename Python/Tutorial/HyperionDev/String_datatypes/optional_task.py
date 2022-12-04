#read a string from the user and store it in the fav_rest
fav_rest = input("Enter your favourite restaurant: ")

#read int value from the user and store it in the fav_rest
int_fav = int(input("Enter your favourite number: "))
 
#print both variables
print(f"Your Favourite Restaurant: {fav_rest}")
print()
print(f"Your Favourite Restaurant: {int_fav}")
 
#convert string to int
print(int(fav_rest)) # This gives error cause the int() function only returns string values.