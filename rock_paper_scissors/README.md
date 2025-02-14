paper_rock_scissors/
│
├── core/                  # Core functionalities
│   ├── __init__.py
│   ├── game.py            # Game logic
│   ├── player.py          # Player class
│   ├── computer.py        # Computer class
│   ├── game_manager.py     # Manages multiple players and game sessions
│   └── logger.py          # Logging utilities
│
├── config.py              # Configuration settings
├── main.py                # Main entry point for the application
├── tests/                 # Test directory
│   ├── test_game.py       # Unit tests for game logic
│   ├── test_player.py     # Unit tests for player logic
│   └── test_game_manager.py# Unit tests for game manager logic
└── README.md              # Project documentation

paper_rock_scissors/
│
├── core/                  # Core functionalities
│   ├── __init__.py
│   ├── game.py            # Game logic
│   ├── player.py          # Player class
│   ├── computer.py        # Computer class
│   └── logger.py          # Logging utilities
│
├── config.py              # Configuration settings
├── main.py                # Main entry point for the application
├── tests/                 # Test directory
│   ├── test_game.py       # Unit tests for game logic
│   ├── test_player.py     # Unit tests for player logic
│   └── test_computer.py   # Unit tests for computer logic
└── README.md              # Project documentation


rock_paper_scissors/
│── app/
│   ├── __init__.py
│   ├── game.py        # Core game logic
│   ├── config.py      # Configurations & constants
│   ├── exceptions.py  # Custom exceptions
│── tests/
│   ├── __init__.py
│   ├── test_game.py   # Unit tests for game logic
│── scripts/
│   ├── start_game.py  # CLI entry point
│── requirements.txt   # Dependencies (if needed)
│── README.md          # Documentation
│── .gitignore         # Ignore unnecessary files
│── pyproject.toml     # Formatting & linting configs
│── .pre-commit-config.yaml # Linting hooks (black, flake8)


rock_paper_scissors/
│── app/
│   ├── __init__.py
│   ├── game.py         # Game engine
│   ├── player.py       # Player models (Human, AI)
│   ├── strategy.py     # AI strategies
│   ├── config.py       # Configurations & constants
│   ├── exceptions.py   # Custom exceptions
│── tests/
│   ├── __init__.py
│   ├── test_game.py    # Unit tests for game logic
│   ├── test_player.py  # Unit tests for players
│   ├── test_strategy.py# Unit tests for AI strategies
│── scripts/
│   ├── start_game.py   # CLI entry point
│── requirements.txt    # Dependencies (if needed)
│── README.md           # Documentation
│── .gitignore          # Ignore unnecessary files
│── pyproject.toml      # Formatting & linting configs
│── .pre-commit-config.yaml # Linting hooks (black, flake8)

rock-paper-scissors/
│── app/                  # Core game logic
│   ├── __init__.py
│   ├── game.py           # Game engine
│   ├── player.py         # Player models (Human, AI)
│   ├── strategy.py       # Strategy pattern for AI decisions
│   ├── exceptions.py     # Custom exceptions
│   └── config.py         # Configurations & constants
│── tests/                # Unit & integration tests (pytest)
│   ├── __init__.py
│   ├── test_game.py      # Tests for game engine
│   ├── test_player.py    # Tests for player models
│   └── test_strategy.py  # Tests for AI strategy
│── scripts/              # Utility scripts (if needed)
│   ├── start_game.py     # CLI Entry point
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── pyproject.toml        # Formatting & linting configs
│── .pre-commit-config.yaml # Linting hooks (black, flake8)
│── .gitignore            # Ignore unnecessary files

rock-paper-scissors/
│── app/                  # Application Code
│   │── __init__.py       # Marks the directory as a package
│   │── game.py           # Core Game Logic
│   │── moves.py          # Move Factory (Strategy Pattern)
│   │── rules.py          # Rule Engine
│   │── interface.py      # Handles User I/O (Decoupled)
│── tests/                # Unit & Integration Tests
│   │── __init__.py       # Marks the directory as a package
│   │── test_game.py      # Pytest-based Tests
│   │── test_moves.py     # Tests for Move Factory
│── scripts/              # Utility scripts (if needed later)
│── configs/              # Configurations (if needed later)
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── main.py               # Entry point for the game