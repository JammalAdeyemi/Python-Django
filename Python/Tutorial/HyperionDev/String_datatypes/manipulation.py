str_manip = input("Enter a sentence: ")

# Calculate and display the length of str_manip.
print(f"The length of your sentence is: {len(str_manip)}")
print()

# Find the last letter in str_manip. Replace every occurrence of this letter in str_manip with ‘@’.
new_str = str_manip.replace(str_manip[-1:], "@")
print(f"String replacement with @: {new_str}")
print()

# Print the last 3 characters in str_manip backwards
last_char = str_manip[:-4:-1]
print(f"last 3 letters backwards are: {last_char}")
print()

# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip.
five_letter = str_manip[0:3] + str_manip[-2:]
print(f"String Manipulation: {five_letter}")
print()

#  Display each word on a new line. I checked online, and implemented what I saw based on my understanding
set_word = str_manip.split()
print("Display each word on a new line:")
for word in set_word:
    print(word)