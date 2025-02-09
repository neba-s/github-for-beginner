# Function-based flight terminal system
def terminal1():
    print("Go from Terminal 1 - Budget Flight")
    main()  # Call the main function again

def terminal2():
    print("Go from Terminal 2 - Domestic Flight")
    main()

def terminal3():
    print("Go from Terminal 3 - International Flight")
    main()

def main():
    flight = input("Is your flight Budget, Domestic, or International? ").lower()
    
    if flight == "budget":
        terminal1()
    elif flight == "domestic":
        terminal2()
    elif flight == "international":  # Fixed typo: 'internation' → 'international'
        terminal3()
    else:
        print("Invalid input. No such terminal available.")

main()  # Start the function loop

# Function to calculate BMI
def bmi(height, weight):
    return weight / (height ** 2)

# Function to provide information based on BMI
def info(bmi_value):
    if bmi_value < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi_value < 25:
        print("You have a normal weight.")
    elif 25 <= bmi_value < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

people = int(input("Enter the number of people: "))

for person in range(people):
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kg: "))
    
    bmi_value = bmi(height, weight)
    print(f"Your Body Mass Index (BMI) is: {bmi_value:.2f}")
    
    info(bmi_value)  # Call the info function
