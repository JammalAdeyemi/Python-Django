import math
#  This program will be used to calculate the area that the foundation of a building covers.

# Ask the user to enter the shape of the building (square, rectangular or round).
print("Enter the shape of the building \n1. Square \n2. Rectangular \n3. Round/Circle")
user = int(input())

if user == 1:
    square_length = float(input("\nEnter the length of the sqaure: "))
    area_square = square_length**2
    print(f"The area of the square is {area_square}.")

elif user == 2:
    rectangle_length = float(input("\nEnter the length of the sqaure: "))
    rectangle_width = float(input("\nEnter the width of the sqaure: "))
    area_rectangle = rectangle_length * rectangle_width
    print(f"The area of the rectangle is {area_rectangle}.")

else:
    circle_radius = float(input("\nEnter the radius of your circle: "))
    area_circle = round(math.pi * (circle_radius**2), 2)
    print(f"The area of the circle is {area_circle}")