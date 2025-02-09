from random import randint

# Get the input from the user, split by spaces to create a list of players
players = input("Enter the names of all players, using a space between each name: ").split(" ")

# Create an empty list to store team numbers
teams = []

# Loop through each player and assign them to a random team from 1 to 3
for i in range(len(players)):
    random_team = randint(1, 3)  # Random team number between 1 and 3
    teams.append(random_team)

# Loop through the players and print their name along with their assigned team number
for i in range(len(players)):
    print(f"{players[i]} is on team {teams[i]}")
