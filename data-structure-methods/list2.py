# Create an empty list for capital cities
capital_cities = []

# Ask the user to enter a city, as long as the user does not enter "quit", the program continues
city = input("Enter the capital cities you know (type 'quit' to stop): ").lower()

while city != "quit":
    # Check if the city has already been entered
    if city in capital_cities:
        print(f"You have already entered {city}!")
    else:
        capital_cities.append(city)  # Add the new city to the list

    # Prompt the user for another city
    city = input("Enter another capital city (type 'quit' to stop): ").lower()

# Sort the list of cities alphabetically
capital_cities.sort()

# Print the sorted list of capital cities
print("Your list of capital cities (sorted):")
print(capital_cities)
