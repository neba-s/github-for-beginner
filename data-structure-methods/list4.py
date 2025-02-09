scores = ["billy-5", "sarah-4", "lio-3", "john-3", "anna-4"]
counter = 0
total = 0  # Renaming 'sum' to 'total' to avoid conflict with built-in function

# Loop through the list and calculate the total score
for score in scores:
    total += int(score.split('-')[1])  # Extract score by splitting at '-' and converting to int
    counter += 1

# Calculate and print the average score
average = total / counter
print(f"The average group score is: {average}")
