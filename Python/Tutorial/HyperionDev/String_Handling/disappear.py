# Write a Python program that strips a set of characters from a string.
# Ask the user to input a string and then ask the user which characters they would like to make disappear.

sentence = input("Enter a sentence: ") 
characters_to_strip = input("Enter the characters you want to strip from the sentence: ")

for i in characters_to_strip:
    sentence = sentence.replace(i, "")
print(sentence)