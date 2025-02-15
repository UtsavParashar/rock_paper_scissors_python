import asyncio
import random
from src.game import Game
import src.constants as const

async def simulate_game(num_rounds):
    """Simulates a game of Rock-Paper-Scissors for a specified number of rounds."""
    game = Game(num_rounds)

    # Simulate human player making random choices
    for _ in range(num_rounds):
        # Randomly choose rock, paper, or scissors
        human_choice = random.choice(const.CHOICES[1:4])  # Exclude 'exit'
        game.player.choose(human_choice)

        # Let the computer choose based on its strategy
        computer_choice = game.computer.strategy.choose(game.player.history)
        game.computer.choose(computer_choice)

        # Determine the winner
        winner = game.rules.determine_winner(human_choice, computer_choice)

        # Update scores based on the outcome
        if winner == const.TIE:
            game.scores[const.TIE] += 1
        else:
            game.scores[winner] += 1

    await game.display_results()

if __name__ == "__main__":
    num_rounds = 10000
    asyncio.run(simulate_game(num_rounds))
