string1 = "he's"
string2 = "probably"
string3 = "pining"
string4 = "for the"
string5 = "fjords"
today = "thursday"

strings = string1 + string2 + string3 + string4 + string5
print(strings)
print()
print("he's" "probably" "pining" "for the" "fjords")
print("Hello " * 5)
print("Hello " * (5+4))
print("Hello " * 5 + "4")
print()
print("day" in today) # True
print("fri" in today) # False
print("thur" in today) # True
print("parrot" in "fjord") # False