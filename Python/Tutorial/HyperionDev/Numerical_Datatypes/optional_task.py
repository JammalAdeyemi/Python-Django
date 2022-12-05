import math
print("Enter the lengths of all 3 sides of a triangle.")
side1 = ("Length 1: ")
side2 = ("Length 2: ")
side3 = ("Length 3: ")
s = (side1 + side2 + side3) / 2
heron = s * (s - side1) * (s - side2) * (s - side3)
area = math.sqrt(heron)

print(f"The area of the triangle is: {area}")