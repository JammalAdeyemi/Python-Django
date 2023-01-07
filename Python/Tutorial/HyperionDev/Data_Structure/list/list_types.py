# Imagine you want to store the names of three of your friends in a list of strings. Create a list variable called friends_names, and write the syntax to 
# store the full names of three of your friends.
friends_name = ["Jammal Adeyemi", "Dexter", "Mohammed Salah"]

# Now, write statements to print out the name of the first friend, then the name of the last friend, and finally the length of the list.
print(f"First friends name is {friends_name[0]}, and the name of my last friend is {friends_name[-1]}. The length of the list is {len(friends_name)}")

# Now, define a list called friends_ages that stores the age of each of your friends in a corresponding manner, i.e., 
# the first entry of this list is the age of the friend named first in the other list.
friends_ages = [24, 31, 32]
for i in range(len(friends_name)):
    print(f"{friends_name[i]} is {friends_ages[i]} years old")
