pupils = []

while True:
    name = input("Enter the name of your pupils in class (type stop to exit): ")
    stop_count = name.lower()
    if stop_count == "stop":
        # exit the loop if the user entered "Stop"
        break
    else:
        # append the name to the list of pupils
        pupils.append(name)
        
# print the total number of names entered by the user
print("Total number of names entered:", len(pupils))