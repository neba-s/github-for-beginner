print("********** Part 2 from the video 'Python for Beginners - Code with Josh' *******************")

# Password verification using a while loop
password = input("Enter your password: ")
while password != "merry_@_my_heart":
    print("You are wrong, please try again.")
    password = input("Enter your password again: ")
print("Welcome to the real world.")

# Item cost calculator with discount
# The user will enter the cost of each item. 
# As long as the user does not enter 0, the code will keep running.
# Once the user enters 0, the total cost is calculated with a 50% discount.

cost = int(input("Enter the cost of an item: "))
total = 0
while cost != 0:
    total += cost
    cost = int(input("Enter the cost of another item (or enter 0 to stop): "))

print("Your total cost after a 50% discount is:", total * 0.5)

# Mini chatbot that accepts messages
message = input("Enter your message, sir. If you are finished, type 'done': ")
while message.lower() != "done":
    message = input("We got your message. Anything else you want to say? ")
print("Thank you for your message.")

# The first 3 people to book get a 20% discount
# Print "Congrats {name}, you saved 20%."
# Once 3 people have received the discount, print "All done."

counter = 0
while counter < 3:
    name = input("Enter your name: ")
    print(f"Congrats {name}, you saved 20%!")
    counter += 1
print("All done.")

# The user must enter a programming language, but they only get 5 tries.
# If they enter "Python", print how many tries it took.

tries = 1
code = input("Enter a programming language: ")
while tries < 5 and code.lower() != "python":
    code = input("Try again. Enter a programming language: ")
    tries += 1 

if code.lower() == "python":
    print(f"It took {tries} tries to get it right.")
else:
    print("Sorry, you ran out of tries!")

# Train ticket booking program
# The program starts when the user enters 1 and ends when they enter 0.
# For every new train ticket, print the ticket number.

booking = input("Enter 1 to book a ticket or 0 to end booking: ")
counter = 1
while booking != "0":
    if booking == "1":  # Ignore invalid inputs
        print(f"Ticket number: {counter}")
        counter += 1
    booking = input("Enter 1 to book a ticket or 0 to end booking: ")

# The range function excludes the last number
print(list(range(2, 5)))  # Output: [2, 3, 4]

# Username validation
# The user cannot enter special characters "!@#$%^&*()"
username = input("Enter your username (special characters !@#$%^&*() are not allowed): ")
invalid_chars = "!@#$%^&*()"

for char in username:
    if char in invalid_chars:
        print(f"You can't use '{char}' in your username.")
        break
else:
    print(f"{username} is a valid username.")

# Count the number of vowels in a word
word = input("Enter a word, and I will tell you how many vowels it has: ")
vowels = "aeiou"
counter = 0

for letter in word.lower():
    if letter in vowels:
        counter += 1

print(f"There are {counter} vowels in the word '{word}'.")
