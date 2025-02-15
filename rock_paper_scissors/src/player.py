import src.constants as const

class Player:
    """Represents a player in the Rock-Paper-Scissors game."""

    def __init__(self, name, strategy=None):
        """Initializes player attributes: name, choice, strategy, and history."""
        self.name = name
        self.choice = None
        self.strategy = strategy
        self.history = []

    def choose(self, choice):
        """Sets the player's choice for the current round, validating it."""
        if choice not in const.CHOICES[1:]:  # Check against valid choices only (excluding exit)
            raise ValueError("Invalid choice. Must be rock, paper, or scissors.")
        self.choice = choice

    def update_history(self, choice):
        """Appends the player's current choice to their history."""
        self.history.append(choice)
