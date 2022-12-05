print("Kindly input 3 different integers")
a = int(input("Integer 1: "))
b = int(input("\nInteger 2: "))
c = int(input("\nInteger 3: "))

#  The sum of all the numbers
summation = a+b+c
print(f"\n{a} + {b} + {c} = {summation}")

#  The first number minus the second number
operation_1 = a - b
print(f"\n{a} - {b} = {operation_1}")

#  The third number multiplied by the first number
operation_2 = c * a
print(f"\n{c} * {a} = {operation_2}")

#  The sum of all three numbers divided by the third number
operation_3 = summation / c
print(f"\nThe sum of all three numbers divided by the third number: {operation_3}")