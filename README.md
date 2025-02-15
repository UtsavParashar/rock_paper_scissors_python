# Rock-Paper-Scissors Game

A production-level Python implementation of the Rock-Paper-Scissors game with an intelligent AI that learns and adapts to human moves.

## Features

* **Intelligent AI:** Employs a combined Reinforcement Learning and Regret Matching strategy for adaptive gameplay.
* **Pre-committed Computer Choice:** Ensures fairness by determining the computer's choice before the human player makes a move.
* **Modular and Extensible:** Designed with a clear separation of concerns, making it easy to add new features or modify existing ones.
* **Industry Standard Directory Structure:** Follows industry best practices for code organization and maintainability.
* **Error Handling and Validation:** Implements robust error handling and input validation to prevent crashes.
* **Memory Efficient and Fast:** Uses lightweight data structures and efficient algorithms for optimal performance.
* **Unit-Tested:** Includes a comprehensive suite of unit tests to ensure robustness and reliability.
* **Asynchronous Operations:** Utilizes `asyncio` and `ThreadPoolExecutor` for handling multiple tasks concurrently, improving responsiveness.

## Design Choices

*   **Object-Oriented Programming:** The game is structured using classes for `Player`, `Rules`, `Strategy`, and `Game`, promoting reusability and maintainability.
*   **Reinforcement Learning and Regret Matching:** The AI employs a combined strategy to adapt to the player's behavior.
*   **Asynchronous Operations:** The game logic is designed to support asynchronous operations, allowing for better responsiveness and scalability.

## Dependencies
Python 3.9+
All package dependencies are listed in the `requirements.txt` file.

## Setup Instructions

1. Go to the repo:

    ```
    cd rock_paper_scissors
    $env:PYTHONPATH = $pwd
    ```

2. Run the setup script:

    ```
    python setup.py install
    ```

3. Create a virtual environment (recommended):

    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

4. Install additional dependencies if needed:

    ```
    pip install -r requirements.txt
    ```

5. Run the game
    ```
    python 
    ```
## Future Enhancements

*   Implement a graphical user interface (GUI).
*   Support network play for multiple human players.
*   Add more sophisticated AI strategies.
*   Incorporate user profiles and personalized game experiences.


