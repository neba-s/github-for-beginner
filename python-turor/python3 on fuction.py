# Local variable: A variable inside a function, only accessible within that function.
# Example: `response` inside `good_deal()` is a local variable.
# Global variable: A variable declared outside a function, accessible throughout the program.
# Example: `item`, `cost`, and `res` are global variables.

def good_deal(cost):
    if 50 <= cost <= 150:
        response = "That is a good deal!"
    elif cost > 150:
        response = "That is very expensive."
    else:
        response = "That is very cheap."
    return response

item = input("What item are you going to buy? ")
cost = int(input("Enter the amount: "))
res = good_deal(cost)  # You can't use `response` here because it's local to the function
print(res)

if res == "That is very cheap.":
    print(f"Buy more {item} before it's too late!")

# Grade Calculator
def grade(score):
    if 0 <= score <= 50:
        print("Below passing, improve your grade.")
    elif 50 < score <= 70:
        print("Barely passing the class.")
    elif 70 < score <= 90:
        print("You have a passing grade.")
    else:
        print("You are the best in the class!")

score = int(input("Enter your score out of 100: "))
grade(score)

# Extra Flight Charge Program
def extra_flight_charge(base_fare):
    upgrade = input("Do you want to upgrade? (yes/no): ")
    if upgrade.lower() == "yes":
        base_fare += 99

    baggage = input("Do you have baggage? (yes/no): ")
    if baggage.lower() == "yes":
        base_fare += 33

    base_fare += 0.08 * base_fare  # 8% additional charge
    return base_fare

base_fare = float(input("Enter the original base fare: "))
print(f"Total fare after charges: {extra_flight_charge(base_fare)}")

# Bank Balance Function
def bank_balance(balance):
    return balance >= 500  # Returns True if balance is 500 or more

customers = int(input("Enter the number of customers: "))

for customer in range(customers):
    name = input("Enter your first name: ")
    balance = int(input("Enter your current balance: "))
    
    if bank_balance(balance):
        print("No need to worry.")
    else:
        print("Your account balance is low.")

# Mortgage Approval Function
def mortgage(balance):
    if balance >= 50000:
        print("Instant approval!")
    elif 20000 <= balance < 50000:
        print("You need approval.")
    else:
        print("Not approved for a mortgage yet...")

deposit_amount = -1  # Start with a non-zero value
total_balance = 0

while deposit_amount != 0:
    deposit_amount = int(input("Enter your deposit amount (0 to stop): "))
    total_balance += deposit_amount
    mortgage(total_balance)

print(f"Your total balance amount is: {total_balance}")
