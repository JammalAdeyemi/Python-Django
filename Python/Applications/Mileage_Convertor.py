# print("How many KM did you cycle today")
kms = input("How many KM did you cycle today: ")
miles = float(kms)/1.60934
rounded_miles = round(miles, 2)
print(f"Your {kms}km ride is {rounded_miles}miles")