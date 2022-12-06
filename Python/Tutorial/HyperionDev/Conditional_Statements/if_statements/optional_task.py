#  Design a program for a department store to calculate the monthly wage for two different types of employees.

print("Job role: \n1. Salesperson \n2. Manager ")
user = int(input())

# Salespeople earn an 8% commission on their gross sales and a fixed salary of R2 000.00 per month. Managers earn an hourly rate of R40.00

# If the user is a salesperson, ask for their gross sales for the month.
if user == 1:
    sales = int(input("Input your gross sales for the month: "))
    commission = sales * 0.08
    fixed_salary = 2000
    salary = fixed_salary + commission
    print(f"\nTotal Salary for the month is {salary}")

# If the user is a manager, ask for the number of hours worked for the month.
elif user == 2:
    hrs = int(input("Input the amount of hrs worked for the month: "))
    hourly_rate = 40
    salary_1 = hrs * hourly_rate
    print(f"\nTotal Salary for the month is {salary_1}")

