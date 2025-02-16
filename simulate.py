import asyncio
import random
import pandas as pd
import concurrent.futures
from src.game import Game
from src import constants as const

async def simulate_game(num_rounds):
    """Simulates a game of Rock-Paper-Scissors for a specified number of rounds."""
    game = Game(num_rounds)

    # Initialize scores
    human_wins = 0
    computer_wins = 0
    ties = 0

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
            ties += 1
        elif winner == const.HUMAN:
            human_wins += 1
        else:
            computer_wins += 1

    return num_rounds, human_wins, computer_wins, ties

def calculate_stats(num_rounds, human_wins, computer_wins, ties):
    """Calculates win percentages."""
    total_rounds = num_rounds
    human_win_percentage = (human_wins / total_rounds) * 100 if total_rounds else 0
    computer_win_percentage = (computer_wins / total_rounds) * 100 if total_rounds else 0
    tie_percentage = (ties / total_rounds) * 100 if total_rounds else 0
    return human_win_percentage, computer_win_percentage, tie_percentage

async def run_simulations(num_rounds_list):
    """Runs simulations for different numbers of rounds in parallel."""
    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                asyncio.run,  # Run asyncio.run in executor
                simulate_game(num_rounds),
            )
            for num_rounds in num_rounds_list
        ]

        for future in asyncio.as_completed(futures):
            num_rounds, human_wins, computer_wins, ties = await future
            human_win_percentage, computer_win_percentage, tie_percentage = calculate_stats(
                num_rounds, human_wins, computer_wins, ties
            )
            results.append({
                "num_rounds": num_rounds,
                "human_wins": human_wins,
                "computer_wins": computer_wins,
                "ties": ties,
                "human_win_percentage": f"{human_win_percentage:.2f}%",
                "computer_win_percentage": f"{computer_win_percentage:.2f}%",
                "tie_percentage": f"{tie_percentage:.2f}%",
            })

    df = pd.DataFrame(results)
    return df

async def main(num_rounds_list):
    """Main function to run simulations and print results."""
    df = await run_simulations(num_rounds_list)
    print(df)

if __name__ == "__main__":
    num_rounds_list = [3, 30, 300, 1000, 3000,]  # Example round numbers
    asyncio.run(main(num_rounds_list))
