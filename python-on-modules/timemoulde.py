# Importing time module
from time import *

"""
The time module has two main functions:
1. time() - Returns the total number of seconds since the beginning of the epoch (January 1, 1970).
2. sleep(seconds) - Pauses the program execution for the given number of seconds.
"""

# Example of time() function
print(time())  # Prints the total seconds since the epoch
print(round(time(), 2))  # Rounds time to 2 decimal places
print(round(time(), 1))  # Rounds time to 1 decimal place
print(round(time()))  # Rounds time to 0 decimal places

# Stopwatch Program
"""
This program acts as a stopwatch:
- User enters "1" to start the timer.
- User enters "0" to stop the timer.
- Points are awarded based on elapsed time:
  - < 10 seconds: 3 points
  - 10-15 seconds: 2 points
  - > 15 seconds: 1 point
"""

timer = int(input("Enter 1 to start and 0 to stop the time: "))
while timer != 0:
    if timer == 1:
        start_timer = time()  # Start timer
    timer = int(input("Enter 1 to start and 0 to stop the time: "))

end_timer = time()  # Stop timer
total = round(end_timer - start_timer, 1)  # Calculate elapsed time
points = 0

# Assign points based on time elapsed
if total < 10:
    points += 3
elif 10 <= total <= 15:
    points += 2
else:
    points += 1

print(f"The time passed is {total} seconds, and you got {points} points.")

# Countdown Clock
"""
This program creates a countdown timer:
- User enters a countdown duration in seconds.
- The program prints the remaining seconds every second.
- At the end, it prints a completion message.
"""

timer = int(input("Enter the countdown time in seconds: "))
while timer > 0:
    print(timer)
    sleep(1)  # Wait for 1 second
    timer -= 1
print("Your countdown has finished!")

# File Download Time Calculator
"""
This program calculates the estimated time to download a file:
- User inputs the internet speed in Mbps (Megabits per second).
- User inputs the file size in MB (Megabytes).
- The program converts file size to Megabits (since 1MB = 8 Megabits).
- It then calculates the estimated download time and starts a countdown.
"""

# Taking user inputs
internet_speed = int(input("Enter the internet speed in Megabits per second (Mbps): "))
file_size = int(input("Enter the file size in Megabytes (MB): "))

# Convert file size to Megabits (1MB = 8 Megabits)
file_size *= 8

# Calculate estimated download time
timer = round(file_size / internet_speed)
print(f"The estimated time to download the file is {timer} seconds.")

# Countdown for download simulation
while timer > 0:
    print(timer)
    sleep(1)
    timer -= 1

print("Download completed!")
