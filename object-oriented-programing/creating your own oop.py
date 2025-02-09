# We are working with the NBA and need a class called Player.
# This class has three properties: name_of_player, score, and team_name.
# The team_name is initially set to None.

# The class should have a method called show_status to display the player's details.
# Another method, select_team, should ask for user input to assign a team name.

class Player:  # Fixed class name typo (Palyer -> Player)
    def __init__(self, name_of_player, score):
        self.name_of_player = name_of_player  # Assign player name
        self.score = score  # Assign player score
        self.team_name = None  # Initialize team_name as None (empty)

    def show_status(self):
        """Displays the player's current details."""
        print(f"Player Name: {self.name_of_player}")
        print(f"Score: {self.score}")
        print(f"Team Name: {self.team_name if self.team_name else 'Not Assigned'}")

    def select_team(self):
        """Prompts the user to enter a team name and updates the team_name property."""
        self.team_name = input("Enter the name of the team: ")  # Assign user input to team_name

# Creating an object for a player
player1 = Player("Messi", 49)  # Fixed typo (messi -> Messi)

# Display initial player details
player1.show_status()

# Select a team for the player
player1.select_team()

# Display updated player details after assigning a team
player1.show_status()
