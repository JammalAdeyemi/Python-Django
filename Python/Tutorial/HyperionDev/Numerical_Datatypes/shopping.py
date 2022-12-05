# Ask the user to enter the names of three products
print("Kindly enter the names of three products")
product1 = input("\nFirst Product: ")
price_1 = float(input("Price in two decimal values: "))
product2 = input("\nSecond Product: ")
price_2 = float(input("Price in two decimal values: "))
product3 = input("\nThird Product: ")
price_3 = float(input("Price in two decimal values: "))

# Calculate the total of all three products
totalBill = price_1 + price_2 + price_3
#print(f"\nTotal price of all 3 products: {totalBill}")

# Calculate the average price of the three products.
avgPrice = round(totalBill/len(str(totalBill)))
#print(f"\nAverage price of the three products: {avgPrice}")

print(f"\nThe Total price of {product1}, {product2}, {product3} is {totalBill} and the average price of the items is {avgPrice}.")