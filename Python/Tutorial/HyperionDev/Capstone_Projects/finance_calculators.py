import math

print("""Choose either 'investment' or 'bond' from the menu to proceed: 
    1. Investment - to calculate the amount of interest you'll earn on your investment.
    2. Bond - to calculate the amount you'll have to pay on a home loan.""")

users_choice = int(input("\n Select 1 or 2: "))

if users_choice == 1:
    amount = int(input("Enter the amount you would like to deposit: "))
    interest_rate = float(input("Enter your interest rate value: "))
    investment_years = float(input("Number of years you plan on investing: "))
    print("Select your preferred interest type \n1. Simple \n2. Compound")
    interest_type = int(input("\n Select 1 or 2: "))
    if interest_type == 1:
        r = interest_rate/100
        simple_interest = amount * (1 + r * investment_years)
        print(f"\nYour Simple Interest Monthly payment will be {simple_interest}")
    else:
        r = interest_rate/100
        compound_interest = amount * math.pow((1 + r), investment_years)
        print(f"\nYour Compound Interest Monthly payment will be {compound_interest}")

else:
    present_value = float(input("Present value of the house: "))
    interest_rate = float(input("Enter your interest rate value: "))
    investment_months = int(input("Number of months you plan to take to repay the bond: "))
    i = interest_rate/12
    bond_interest = (i * present_value)/(1 - math.pow((1 + i), -investment_months))
    print(f"\nYour Bond repayment will be {bond_interest}")
