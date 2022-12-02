parrot = "Norwegian Blue"

print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()
# Using Negative slicing
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()

## Slicing [star:stop:step]
print(parrot[0:6]) # Norweg
print(parrot[3:5]) # we
print(parrot[:9]) # Norwegian
print(parrot[10:14]) # Blue
print(parrot[10:]) # Blue
print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw
print()

# Slicing with negative numbers
print(parrot[-4:-2]) # BL
print(parrot[-4:12]) # BL
print()

number = "9,222;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

# To get the values in number
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
print()

# Sliceback
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
print(backwards)
print(letters[16:13:-1]) #qpo
print(letters[4::-1]) # edcba
print(letters[:17:-1]) # Last 8 characters in reverse order

d = dict(zip("abc", [1,2,3]))
print(d)
