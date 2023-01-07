# Imagine you are running a cafe. 

# Create a list called menu, which should contain at least 4 items in the cafe.
menu = ['coffee', 'tea', 'sandwich', 'cake']

# Next, create a dictionary called stock, which should contain the stock value for each item on your menu.
stock = {'coffee': 15, 'tea': 10, 'sandwich': 20, 'cake': 25}

# Create another dictionary called price, which should contain the prices for each item on your menu.
price = {'coffee': 2.4, 'tea': 1.5, 'sandwich': 3.5, 'cake': 4.0}

# Next, calculate the total stock worth in the cafe. You will need to remember to loop through the appropriate dictionaries and lists to do this.
stock_worth = 0
for item in menu:
    stock_worth += stock[item] * price[item]

# Finally, print out the result of your calculation.
print(f'The total stock worth in the cafe is £{stock_worth:.2f}')

