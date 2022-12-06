# You need to design a program for a courier company to calculate the cost of sending a parcel.

# Ask the user to enter the price of the package they would like to purchase.
package_price = input("Enter the price of the package you would like to purchase: ")

# Ask the user to enter the total distance of the delivery in kms.
total_distance = print("\nEnter the delivery total distance in kms: ")

# Now add on the delivery costs to get the final cost of the product
print("\nShipping Method:\n1. Air Shipping \n2. Freight Shipping")
c = int(input())
cost = 0
if c == 1:
    cost = 0.36
elif c == 2:
    cost = 0.25

print("\nInsurance type:\n1. Full insurance \n2. limited insurance")
c1=int(input())
ins_cost = 0
if c1 == 1:
    ins_cost = 50
elif c1 == 2:
    ins_cost = 25

print("\nSelect if you want to add a gift:\n1. Yes \n2. No")
c2=int(input())
g_cost = 0
if c2 == 1:
    g_cost = 15
elif c2 == 2:
    g_cost = 0

print("\nDelivery type:\n1. Priority delivery \n2. Standard delivery")
c3=int(input())
deli_cost=0
if c3 == 1:
    deli_cost = 100
elif c3 == 2:
    deli_cost = 20

total = package_price + (total_distance * cost) + ins_cost + g_cost + deli_cost

print("\nTotal cost for the package is: ",total)