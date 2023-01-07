#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
'''This is the section where you will write code to allow a user to login to the system.'''

while True:
    login = input('Enter your username: ')
    password = input('Enter your password: ')

    with open('user.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            details = line.split(', ')
            user_login = details[0].strip()
            user_password = details[1].strip()
            if login == user_login and password == user_password:
                print('Welcome to the Task Manager')
                pass
            else: 
                print('Wrong username or password, please try again')
                exit()            

    while True:
        #presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()

        if menu == 'r':
            # Requesting input of a new username
            new_user = input('Enter a new username: ')
            # Requesting input of a new password
            new_password = input('Enter a new password: ')
            # Requesting input of password confirmation
            confirm_password = input('Confirm your password: ')
            # Checking if the new password and confirmed password are the same.
            if new_password == confirm_password:
                with open('user.txt', 'a') as file:
                    file.write(f'\n{new_user}, {new_password}')      
            else:
                print('Password does not match, please try again')
            pass

        elif menu == 'a':
            # Request the user to input the username of the person the task is assigned to
            assigned_user = input('Enter the username of the person the task is assigned to: ')

            # Request the user to input the title of the task
            task_title = input('Enter the title of the task: ')

            # Request the user to input the description of the task
            task_description = input('Enter the description of the task: ')

            # Request the user to input the due date of the task
            task_due_date = input('Enter the due date of the task: ')

            # Request the user to input the current date
            current_date = input('Enter the current date: ')

            # Request the user to input the status of the task
            task_status = input('Enter the status of the task: ')

            # Write the data to the task.txt file
            with open('task.txt', 'a') as file:
                file.write(f'{assigned_user}, {task_title}, {task_description}, {task_due_date}, {current_date}, {task_status}\n')
            pass


        elif menu == 'va':
            # Read a line from the file
            with open('task.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    details = line.split(', ')
                    print(f'Assigned to: {details[0].strip()}')
                    print(f'Task: {details[1].strip()}')
                    print(f'Date assigned: {details[4].strip()}')
                    print(f'Due Date: {details[3].strip()}')
                    print(f'Task Status: {details[5].strip()}')
                    print(f'Task Description: {details[2].strip()}')
                    print('')

            pass
            '''In this block you will put code so that the program will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
                - Read a line from the file.
                - Split that line where there is comma and space.
                - Then print the results in the format shown in the Output 2 
                - It is much easier to read a file using a for loop.'''

        elif menu == 'vm':
            # Read a line from the file
            with open('task.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    details = line.split(', ')
                    if login == details[0].strip():
                        print(f'Assigned to: {details[0].strip()}')
                        print(f'Task: {details[1].strip()}')
                        print(f'Date assigned: {details[4].strip()}')
                        print(f'Due Date: {details[3].strip()}')
                        print(f'Task Status: {details[5].strip()}')
                        print(f'Task Description: {details[2].strip()}')
                        print('')
                    else:
                        print('No task assigned to you')
                        break
            pass
            '''In this block you will put code the that will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the username you have
                read from the file.
                - If they are the same print it in the format of Output 2 in the task PDF'''

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")