# This section demonstrates inheritance and the use of a superclass.

class Agent:  # Fixed class name (agent -> Agent) to follow proper naming conventions
    def __init__(self, name, health, car):
        self.name = name  # Assign agent's name
        self.health = health  # Assign agent's health
        self.car = car  # Assign agent's car

    def info(self):
        """Displays the agent's details."""
        print(f"Welcome: {self.name}")
        print(f"Your health: {self.health}")
        print(f"Your choice of car: {self.car}")

# The Spy class inherits from the Agent class
class Spy(Agent):  # Fixed class name (spy -> Spy)
    def spy_talk(self):
        """Spy introduces themselves."""
        print(f"My name is {self.name}")

    def shoot(self, bad_guy):
        """Shoots an enemy agent, reducing their health."""
        if bad_guy.health > 0:
            bad_guy.health -= 20
            print(f"{bad_guy.name} has lost 20 health points. Remaining health: {bad_guy.health}")
        else:
            print(f"{bad_guy.name} is already out of health!")

# Creating spy and agent objects
nebiyu = Spy("Nebiyu", 100, "Mercedes")  # Fixed spelling (merccides -> Mercedes)
negasi = Agent("Negasi", 50, "Jaguar")  # An agent object (or could be a Spy since spies can shoot spies or agents)

# Display spy details
nebiyu.info()

# Nebiyu shoots himself (this is just for testing, usually a spy wouldn't do this!)
nebiyu.shoot(nebiyu)
