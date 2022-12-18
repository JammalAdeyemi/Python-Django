# String Indexing
String = "Hello"
print(String[0]) # H
print(String[1]) # e
print(String[2]) # l
print(String[3]) # l
print(String[4]) # o
print()

original_string = "Hello world!"
new_string = original_string[0:5]
print(new_string)
print()

# STRING BUILDING
number_builder = ""
i = 0
while i <= 50:
    if i % 2 == 0:
        number_builder += str(i) + " "
    i += 1
print("Example 3: ")
print(number_builder)

number_builder = []
i = 0
while i <= 50:
    if i % 2 == 0:
        number_builder.append(str(i))
    i += 1
print("Example 4:")
print(" ".join(number_builder))