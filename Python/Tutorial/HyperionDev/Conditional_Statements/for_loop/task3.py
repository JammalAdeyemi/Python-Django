# Create a while loop that will display count down from 20 to 0.
x = 20
while x >= 0:
    print(x, end = " ")
    x -= 1
print()

#  create a loop (any) that will display all the even numbers between 1 and 20
start, end = 1, 20
# iterating each number in list
for num in range(start, end + 1):   
    # checking condition
    if num % 2 == 0:
        print(num, end = " ")
print()

given_number = 5
stars = ""
for i in range(0, given_number):
    stars += "*"
    print(stars)
print()

#  write the code to compute the greatest common divisor (GCD, or highest common factor) of two positive integers.
# Prompt the user to enter two positive integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Initialize the GCD to the smaller of the two integers
gcd = min(a, b)

# Loop through the possible divisors of the integers
for i in range(gcd, 0, -1):
  # Check if the current divisor is a common divisor of both integers
  if a % i == 0 and b % i == 0:
    # Set the GCD to the current divisor
    gcd = i
    break

# Print the GCD
print(f"The GCD of {a} and {b} is {gcd}")
