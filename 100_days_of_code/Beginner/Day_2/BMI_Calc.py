# Exercise - BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height2 = float(height) * float(height)

BMI = int(weight) / height2

print(round(BMI))