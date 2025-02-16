# Rock-Paper-Scissors Game

A production-level Python implementation of the Rock-Paper-Scissors game for an human to play against an intelligent model using Reinforcement learning and Markov model that learns and adapts to human moves. 
Game Theory strategy could also be used along with existing strategies for better user engagement game.


## Features

- **Engaging Gameplay:** Play the classic game of Rock-Paper-Scissors against an intelligent Computer opponent.
- **Adaptive Strategies:** Computer program uses a combined strategy leveraging Reinforcement Learning and Markov Models to learn and adapt to your playing style.
- **Reinforcement Learning:** The program learns from past games, improving its decision-making over time through a Q-learning approach.
- **Markov Model Prediction:** The program analyzes your move history using a Markov model to predict your next move based on patterns.
- **Customizable History Length:** Adjust the length of the move history used by the computer to influence its predictive capabilities.
- **Exploration vs. Exploitation:** Balances exploration of new strategies with exploitation of learned patterns for optimal performance.
- **Detailed Game Output:** View a clear record of each round, including your choice, the computer's choice, and the outcome.
- **Comprehensive Unit Tests:** Ensures code reliability and correctness through a suite of automated tests.

## Technical Design Choices

- **Modular Architecture:** The project is organized into distinct modules, each responsible for a specific aspect of the game. This modularity enhances code maintainability and readability. Key modules include:
  - `game.py`: Manages the game flow and interactions between players.
  - `player.py`: Defines player behavior and attributes.
  - `rules.py`: Implements the game rules and determines outcomes.
  - `strategy.py`: Contains strategies for decision-making.
  - `constants.py`: Centralizes constant values used throughout the project.

- **Design Patterns:**
  - **Strategy Pattern:** Utilized to encapsulate various AI decision-making strategies. This allows for easy swapping and testing of different strategies without modifying the core game logic, promoting flexibility and scalability.
  - **Observer Pattern:** Implemented to notify players of game state changes (e.g., when a round ends or a player wins). This decouples the game logic from the user interface, allowing for easier updates and modifications to either component independently.

- **Test-Driven Development (TDD):** The project follows a test-driven development approach, ensuring that tests are written before implementing features. This practice helps in defining clear requirements and facilitates refactoring while maintaining functionality.

- **Comprehensive Unit Testing:** The project includes a suite of unit tests that cover critical components and functionalities. Each module has corresponding tests that validate its behavior, ensuring code reliability and reducing the likelihood of bugs.

- **Documentation:** Inline comments and docstrings are used throughout the codebase to explain complex logic and provide context for future developers. Additionally, a comprehensive README file outlines project setup, usage, and features.


## Python Scripts in `src/`

-   **`__init__.py`**: An empty file that signifies the `src` directory is a Python package, allowing its modules to be imported. It follows Python's packaging conventions, enabling modular code organization.
-   **`game.py`**: Contains the main game logic, orchestrating the game flow between the human player and the AI. It uses the Strategy pattern to allow different AI strategies to be plugged in and the Facade pattern to simplify the interaction with underlying modules.
-   **`player.py`**: Defines the `Player` class, representing either the human or computer player, storing their choices and history. It is a simple data class, following object-oriented principles for encapsulation of player-related data and actions.
-   **`rules.py`**: Implements the game rules to determine the winner of each round based on the players' choices. It uses a straightforward conditional logic, following best practices for clear and maintainable code.
-   **`strategy.py`**: Defines the AI's strategy using a combination of Reinforcement Learning, Markov Model. It leverages the Strategy pattern, and adopts a combined approach to make the AI competitive and adaptable.
-   **`constants.py`**: Stores constant values used throughout the project, such as player choices and outcomes. It follows the best practice of centralizing configuration to improve maintainability.



## Dependencies
Python 3.7+
All package dependencies are listed in the `requirements.txt` file.

## Setup Instructions

1. Go to the project directory:

    ```
    cd rock_paper_scissors
    $env:PYTHONPATH = $pwd
    ```

2. Create a virtual environment (recommended/optional):

    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3. Install additional dependencies if needed:

    ```
    pip install -r requirements.txt
    ```

5. Run the game
    ```
    python src/game.py
    ```

## Testing

To run the unit tests for this project:

1. Navigate to the root directory of the project (the one containing the `tests` folder).
```
    cd rock_paper_scissors
```

2. Run the tests using `pytest`:
```
    python -m pytest -v
```

## `simulate.py`

This script runs multiple simulations of the Rock-Paper-Scissors game with varying numbers of rounds, providing data on win rates. It leverages parallel processing to speed up simulations and presents results in a Pandas DataFrame.

1. Run simulate.py
1. Navigate to the root directory of the project (the one containing the `tests` folder).
```
    cd rock_paper_scissors
```

2. Run the tests using `pytest`:
```
    python simulate.py
```
Sample Test Results
   num_rounds  human_wins  computer_wins  ties human_win_percentage computer_win_percentage tie_percentage
0          30          12             11     7               40.00%                  36.67%         23.33%
1         300          92             97   111               30.67%                  32.33%         37.00%
2           3           1              1     1               33.33%                  33.33%         33.33%
3        1000         329            326   345               32.90%                  32.60%         34.50%
4        3000         995            980  1025               33.17%                  32.67%         34.17%


## Future Enhancements

*   Implement a graphical user interface (GUI).
*   Support network play for multiple human players.
*   Add more sophisticated strategies.
*   Incorporate user profiles and personalized game experiences.
*   Extend the game to support additional moves (e.g., Rock Paper Scissors Lizard Spock).


