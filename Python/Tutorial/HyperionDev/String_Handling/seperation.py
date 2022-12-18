# Write a program that inputs a sentence and then displays each word of the sentence on a separate line.

sentence = input("Enter a sentence: ") 

for word in sentence.split():
    print(word)
    