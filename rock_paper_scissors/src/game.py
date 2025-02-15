import asyncio
import concurrent.futures
import random

from src.player import Player
from src.rules import Rules
from src.strategy import CombinedStrategy
from src.utils import get_valid_choice
import src.constants as const

class Game:
    """Manages the Rock-Paper-Scissors game flow."""

    def __init__(self, num_rounds=3):
        """Initializes the game environment with players and rules."""
        self.num_rounds = num_rounds
        self.player = Player(const.HUMAN)
        self.computer = Player(const.COMPUTER, strategy=CombinedStrategy())
        self.rules = Rules()
        self.round_number = 0
        self.scores = {const.HUMAN: 0, const.COMPUTER: 0, const.TIE: 0}
        self.executor = concurrent.futures.ThreadPoolExecutor()
        self.history = []  # Add history

    async def get_human_choice(self):
        """Prompts and validates the human player's choice asynchronously."""
        prompt = f"Enter your choice (1 for {const.CHOICES[1]}, 2 for {const.CHOICES[2]}, 3 for {const.CHOICES[3]}, or '{const.EXIT_CHOICES[0]}'/'exit' to exit): "
        choice = await asyncio.to_thread(get_valid_choice, prompt, const.VALID_INPUTS)
        if choice in ["1", "2", "3"]:
            return const.CHOICES[int(choice)]
        return choice

    async def play_round(self):
        """Orchestrates a single round of Rock-Paper-Scissors gameplay."""
        self.round_number += 1
        print(f"\nRound {self.round_number}:")

        human_choice = await self.get_human_choice()

        if human_choice == const.CHOICES[0]:
            print("Exiting the game...")
            await self.display_results()
            return False

        self.player.choose(human_choice)
        computer_choice = self.computer.strategy.choose(self.history)
        self.computer.choose(computer_choice)

        print(f"You chose: {self.player.choice}")
        print(f"Computer chose: {self.computer.choice}")

        winner = self.rules.determine_winner(self.player.choice, self.computer.choice)

        if winner == const.TIE:
            print("It's a tie!")
            self.scores[const.TIE] += 1
        else:
            if winner == const.HUMAN:
                print("You won!")
            else:
                print(f"{winner} wins the round!")
            self.scores[winner] += 1

        self.computer.strategy.update_rewards(computer_choice, self.player.choice, self.history)
        self.history.append(human_choice)

        return True

    async def play_game(self):
        """Manages gameplay across multiple rounds until completion or exit."""
        print("Welcome to Rock-Paper-Scissors!")

        while self.round_number < self.num_rounds:
            continue_game = await self.play_round()
            if not continue_game:
                break

        if self.round_number == self.num_rounds:
            await self.display_results()

    async def display_results(self):
        """Displays final results of gameplay including scores, ties, and total rounds."""
        print("\nGame Over!")
        print(f"Final Score - You: {self.scores[const.HUMAN]}, Computer: {self.scores[const.COMPUTER]}, Ties: {self.scores[const.TIE]}")
        print(f"Total Rounds Played: {self.round_number}")

        if self.scores[const.HUMAN] > self.scores[const.COMPUTER]:
            print("Congratulations, you won the game!")
        elif self.scores[const.HUMAN] < self.scores[const.COMPUTER]:
            print("The computer won the game!")
        else:
            print("The game ended in a tie!")

async def main():
    """Main entry point to run the game."""
    num_rounds = int(input("How many rounds do you want to play? "))
    game = Game(num_rounds)
    await game.play_game()

if __name__ == "__main__":
    asyncio.run(main())
