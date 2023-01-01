# We will write a program called student_register.py that allows students to register for an exam venue.

# First, ask the user how many students are registering.
num_students = int(input("How many students are registering? "))

# Write each of the ID numbers to a Text File called reg_form.txt
with open('reg_form.txt', 'w+') as file:
    # Create a for loop that runs for that amount of students.
    for i in range(num_students):
        # Each time the loop runs it needs to ask the next student to enter their ID number.
        id_num = input("Enter your ID number: ")
        # Write the ID number to the file
        file.write(id_num + '\n')
        # Include a dotted line to sign because this document will be used as an attendance register which the students will sign when they arrive at the exam venue.
        file.write('-------------------\n')
        # file.close()

# Print a message to confirm that the IDs have been written to the file
print("ID numbers written to reg_form.txt")


