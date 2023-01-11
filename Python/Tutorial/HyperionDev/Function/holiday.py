# You will need to create four functions

# hotel_cost — This function will take the number of nights a user will be staying at a hotel as an argument, and return a total cost for the hotel stay 
# (You can choose the price per night charged at the hotel).
def hotel_cost(nights):
    price_per_night = 100
    total_cost = price_per_night * nights
    return total_cost


# plane_cost — This function will take the city you are flying to as an argument and return a cost for the flight 
# (Hint: use if/else if statements in the function to retrieve a price based on the chosen city).
def plane_cost(city):
    if city == "london":
        return 100
    elif city == "paris":
        return 150
    elif city == "new york":
        return 200
    else:
        print("Invalid city")

# car_rental — This function will take the number of days the car will be hired for as an argument and return the total cost of the car rental.
def car_rental(days):
    price_per_day = 50
    total_cost = price_per_day * days
    return total_cost

# holiday_cost — This function will take three arguments: the number of nights a user will be staying in a hotel, the city the user will be flying to, 
# and the number of days that the user will be hiring a car for. Using these three arguments, you can call all three of the above functions with respective arguments 
# and finally return a total cost for your holiday.
def holiday_cost(nights, city, days):
    hotel_expense = hotel_cost(nights)
    flight_expense = plane_cost(city)
    car_expense = car_rental(days)
    total_expense = hotel_expense + flight_expense + car_expense
    return total_expense

nights = int(input("How many nights are you staying? "))
city = input("What city are you flying to? ").lower()
days = int(input("How many days are you hiring a car for? "))
total_cost = holiday_cost(nights, city, days)
print("Holiday details:")
print(f" - Hotel: {nights} nights at ${hotel_cost(nights)} total")
print(f" - Flight: to {city} at ${plane_cost(city)}")
print(f" - Car rental: {days} days at ${car_rental(days)} per day")
print(f"Total cost of holiday: ${total_cost}")
