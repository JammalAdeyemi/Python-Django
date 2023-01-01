with open('DOB.txt', 'r+') as file:
    data = file.readlines()

# Initialize two lists to store the names and birthdates
names = []
birthdates = []

for line in data:
    details = line.split()
    names.append(details[:2])
    birthdates.append(details[2:])

# Print the names and birthdates
print("Name")
for name in names:
    print("{}".format(" ".join(name)))

print("\nBirthdate")
for birthdate in birthdates:
  print("{}".format(" ".join(birthdate)))
