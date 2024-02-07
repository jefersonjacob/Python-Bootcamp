def hotel_cost(num_nights):
    # Assuming a hotel cost of $100 per night
    return num_nights * 100

def PLANE_COST(city_flight):
    # Define different flight costs based on cities
    
    while True:
        if city_flight.lower() == "new york":
            return 300
        elif city_flight.lower() == "los angeles":
            return 400
        elif city_flight.lower() == "london":
            return 500
        else:
            print("Please select city from the option: ")
            city_flight = input("Enter the city you will be flying to (New York, Los Angeles, London): ")

def car_rental(rental_days):
    # Assuming a daily car rental cost of $50
    return rental_days * 50

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# Getting user inputs
city_flight = input("Enter the city you will be flying to (New York, Los Angeles, London): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car: "))


# Calculating costs
hotel_total = hotel_cost(num_nights)
PLANE_TOTAL = PLANE_COST(city_flight)
car_total = car_rental(rental_days)
total_cost = holiday_cost(hotel_total, PLANE_TOTAL, car_total)

# Print holiday details
print("\nHoliday Details:")
print(f"City of Flight: {city_flight.upper()}")
print(f"Number of Nights in Hotel: {num_nights}")
print(f"Number of Rental Days for Car: {rental_days}")
print(f"Hotel Cost: ${hotel_total}")
print(f"Flight Cost: ${PLANE_TOTAL}")
print(f"Car Rental Cost: ${car_total}")
print(f"Total Holiday Cost: ${total_cost}")
