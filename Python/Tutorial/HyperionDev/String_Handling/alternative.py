#  Create a program that reads in a string and makes each alternate character an uppercase character and each other alternate character
#  a lowercase character (e.g, the string “Hello World” would become “HeLlO WoRlD”)

sentence = input("Enter a sentence: ") 
output = ""

for i in range(len(sentence)):
    if i % 2 == 0:
        output += sentence[i].upper()
    else:
        output += sentence[i].lower()

print(output)