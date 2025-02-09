"""
This script demonstrates the usage of the `random` module and includes:
1. Generating random numbers (float & integer).
2. Shuffling a list randomly.
3. Assigning passengers to random flights.
4. A simple number guessing game.
"""

# Importing all functions from the `random` module
from random import *

# Example of generating random numbers and shuffling a list
names_list = ["Sara", "Yalemgeta", "Amanuel", "Almaz"]  # Fixed variable name (list -> names_list)
print(random())  # Generates a random float number between 0 and 1
print(randint(4, 9))  # Generates a random integer between 4 and 9
shuffle(names_list)  # Shuffles the list randomly
print(names_list)  # Prints the shuffled list

# Passenger Assignment to Flights
"""
This program assigns passengers randomly to two different flights.
- It asks users if they want a new flight.
- If the answer is "no", the program stops.
- Otherwise, a random flight (1 or 2) is assigned to a passenger.
- It keeps track of how many passengers are assigned to each flight.
"""

# Initialize passenger counters
counter_1 = 0
counter_2 = 0

# Ask the user if they want a new flight
ask = input("Do you want a new flight? (yes/no): ")

while ask.lower() != "no":  # Loop continues unless the user enters "no"
    random_flight = randint(1, 2)  # Randomly assign a flight (either 1 or 2)
    print(f"Flying number is: {random_flight}")
    
    if random_flight == 1:
        counter_1 += 1  # Increment flight 1 counter
    else:
        counter_2 += 1  # Increment flight 2 counter

    ask = input("Do you want a new flight? (yes/no): ")  # Ask again

# Display the number of passengers assigned to each flight
print(f"The number of passengers on Flight 1 is {counter_1}.")
print(f"The number of passengers on Flight 2 is {counter_2}.")

# Guessing Game
"""
This program generates a random number between 0 and 10, and the user must guess it.
- If the guess is too low, it prints "Too low!"
- If the guess is too high, it prints "Too high!"
- The game continues until the user guesses correctly.
- It tracks the number of attempts.
"""

# Generate a secret random number
secret = randint(0, 10)
tries = 1  # Counter for number of attempts

# User input
guess = int(input("Enter a number between 0 and 10: "))

while guess != secret:  # Loop until the user guesses correctly
    if guess < secret:
        print("Too low!")  # Hint if guess is too small
    elif guess > secret:
        print("Too high!")  # Hint if guess is too large
    
    tries += 1  # Increase attempt count
    guess = int(input("Enter a number between 0 and 10: "))  # Ask again

# Display success message
print(f"You got it! Congratulations! It took you {tries} tries.")
