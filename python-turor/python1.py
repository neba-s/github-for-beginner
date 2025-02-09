# Display course information
print("********* This course is taken from YouTube video 'Code with Josh - Python for Beginners (13 Hours)' ********")

# A comma (,) automatically creates a space in the output.
print("hello", "world")
print(45, 3)

# In Python, calculations follow the PEMDAS rule:
# P (Parentheses) → E (Exponents) → M (Multiplication) → D (Division) → A (Addition) → S (Subtraction)

# Variable names must begin with a letter.
book1 = 200  # Correct
# 1book = 200  # Incorrect (This would cause an error)

# Resort discount calculation
# A resort normally charges $500 per night. A family wants to stay for one week.
# There is a 30% discount on the total price.

resort_price = 500  # Price per night
stay_days = 7  # Number of days staying
discounted_price = 0.7 * (resort_price * stay_days)  # Applying 30% discount

print("The total price with a 30% discount is:", discounted_price)

# Always remember: When accepting user input and performing calculations,
# convert the input into an integer or float because input() returns a string.

id_number = input("Enter your ID: ")
if id_number == "1116":  # Always compare strings with strings
    print("You are correct.")
else:
    print("You are not correct.")

# Nested Function Example:
# Functions like print(), int(), len(), input() can be used inside each other.

print(int(len(input("Enter your grandfather's name: "))))  # Get the length of the input and convert it to an integer.

# String Methods: lower(), upper(), capitalize()
# These methods do not modify the original string; they return a new string.

name = "NeBiyu"
print(name)  # Original string
print(name.lower())  # Convert all characters to lowercase
print(name.upper())  # Convert all characters to uppercase
print(name.capitalize())  # Capitalize the first letter and make the rest lowercase
print(name)  # The original string remains unchanged.

# Instead of using if, elif, else, you can also use multiple if statements.
# This works like checking multiple conditions independently.

# Discount Based on Product Prices:
# Ask the user for the price of three different products.
# If the third product is the most expensive, apply a 50% discount.
# If the first product is the most expensive, apply a 30% discount.
# Print the final total.

price1 = int(input("Enter the price of the first product: "))
price2 = int(input("Enter the price of the second product: "))
price3 = int(input("Enter the price of the third product: "))

total = price1 + price2 + price3

if price3 > price1 and price3 > price2:
    print("Discount applied: 50% off!")
    total *= 0.5  # Apply a 50% discount

if price1 > price2 and price1 > price3:
    print("Discount applied: 30% off!")
    total *= 0.7  # Apply a 30% discount

print("Total price after discount:", total)
