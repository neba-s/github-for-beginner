"""
This module contains two functionalities:
1. Flight Terminal Selection: Determines which terminal a passenger should go to based on their flight type.
2. BMI Calculator: Calculates Body Mass Index (BMI) and provides health category feedback.
"""

# Flight Terminal Selection Module
def terminal1():
    """Handles budget flights."""
    print("Go to Terminal 1 - Budget")
    main()  # Return to main function for another input

def terminal2():
    """Handles domestic flights."""
    print("Go to Terminal 2 - Domestic")
    main()  

def terminal3():
    """Handles international flights."""
    print("Go to Terminal 3 - International")
    main()  

def main():
    """Main function to determine the correct terminal based on user input."""
    flight = input("Is your flight budget, domestic, or international? ").strip().lower()
    
    if flight == "budget":
        terminal1()
    elif flight == "domestic":
        terminal2()
    elif flight == "international":  # Fixed spelling (internation → international)
        terminal3()
    else:
        print("Invalid input! No such terminal.")

# BMI Calculator Module
def bmi(height, weight):
    """Calculates BMI using the formula: weight (kg) / (height (m)²)."""
    body_mass_index = weight / (height ** 2)
    return body_mass_index

def info(bmi_value):
    """Determines the weight category based on BMI value."""
    if bmi_value < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi_value < 25:
        print("You have a normal weight.")
    elif 25 <= bmi_value < 30:
        print("You are overweight.")
    else:
        print("You are obese.")
