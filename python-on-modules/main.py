"""
This script explains different ways to import modules and demonstrates their usage.

1. `import random` → Imports the entire module (must specify `random.function_name` when using functions).
2. `from random import shuffle` → Imports only the `shuffle` function (more efficient for large modules).
3. `from random import *` → Imports everything from the module (not recommended for large libraries as it can slow down the system).

Modules make code easier to understand and write by promoting reusability.
"""

# Importing all functions from the 'function' module
from fuction import *

# Calling the main function from the imported module
main()  # This nested function structure behaves similarly to a loop since functions call each other.

# BMI Calculation for multiple people
people = int(input("Enter the number of people: "))  # Ask for the number of individuals

# Loop through each person and calculate BMI
for person in range(people):
    height = float(input("Enter your height in meters: "))  # Input height
    weight = float(input("Enter your weight in kg: "))  # Input weight
    bmi_value = bmi(height, weight)  # Calculate BMI using the imported function
    print(f"Your Body Mass Index (BMI) is {bmi_value:.2f}")  # Display BMI with two decimal places
    info(bmi_value)  # Determine BMI category using the imported function
