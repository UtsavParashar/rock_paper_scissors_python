CHOICES = ["exit", "rock", "paper", "scissors"]
"""
A list of valid choices in the game.
Index 0 corresponds to 'exit', allowing players to quit the game.
Indices 1, 2, and 3 correspond to 'rock', 'paper', and 'scissors' respectively.
This structure allows easy reference to choices by index.
"""

VALID_INPUTS = ["1", "2", "3", "rock", "paper", "scissors", "0", "exit"]
"""
A list of all valid inputs that a user can enter to make a choice in the game.
Includes numeric representations ("1" for rock, "2" for paper, "3" for scissors)
as well as their string equivalents and exit options ("0" and "exit").
This enables flexible user input.
"""

EXIT_CHOICES = ["0", "exit"]
"""
A list containing valid inputs that allow the player to exit the game.
Includes both "0" and "exit" to provide options for quitting.
"""

TIE = "tie"
"""
A constant representing a tie outcome in the game.
Used in comparisons to determine if both players have made the same choice.
"""

HUMAN = "Human"
"""
A constant representing the human player in the game.
"""

COMPUTER = "Computer"
"""
A constant representing the computer player in the game.
"""

WIN = 1
"""
An integer constant representing a win reward in reinforcement learning strategy.
"""

LOSE = -1
"""
An integer constant representing a loss reward in reinforcement learning strategy.
"""

TIE_REWARD = 0
"""
An integer constant representing the reward for a tie in reinforcement learning strategy.
"""