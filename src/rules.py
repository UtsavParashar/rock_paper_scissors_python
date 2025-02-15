import src.constants as const

class Rules:
    """Defines the rules of Rock-Paper-Scissors."""

    def determine_winner(self, player_choice, computer_choice):
        """Determines the winner of the round based on player and computer choices."""
        if player_choice == computer_choice:
            return const.TIE

        if ((player_choice == const.CHOICES[1] and computer_choice == const.CHOICES[3]) or
            (player_choice == const.CHOICES[2] and computer_choice == const.CHOICES[1]) or
            (player_choice == const.CHOICES[3] and computer_choice == const.CHOICES[2])):
            return const.HUMAN

        return const.COMPUTER
