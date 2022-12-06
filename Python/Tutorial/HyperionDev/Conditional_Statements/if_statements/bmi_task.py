# Create a program that calculates a person's BMI

# Ask the user to enter their weight in kg and their height in m
user_weight = int(input("Enter your weight(KG): "))
user_height = int(input("\nInput you height(m): "))

BMI = round(user_weight / (user_height ** 2),1)
if BMI >= 30:
    print(f"\nYou have a BMI of {BMI}, which means you are obese.")
elif BMI >= 25:
    print(f"\nYou have a BMI of {BMI}, which means you are overweight.")
elif BMI >= 18.5:
    print(f"\nYou have a BMI of {BMI}, which means you are normal.")
else:
    print(f"\nYou have a BMI of {BMI}, which means you are underweight.")


