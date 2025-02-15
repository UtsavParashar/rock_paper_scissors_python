import pytest
import asyncio
from src.game import Game
import src.constants as const

@pytest.mark.asyncio
async def test_game_initialization():
    """Test that the game initializes with the correct default values."""
    game = Game(num_rounds=3)
    assert game.num_rounds == 3
    assert game.round_number == 0
    assert game.scores[const.HUMAN] == 0
    assert game.scores[const.COMPUTER] == 0
    assert game.scores[const.TIE] == 0

@pytest.mark.asyncio
async def test_play_round(capsys):
    """Test the play_round function."""
    game = Game(num_rounds=1)
    game.player.choose(const.CHOICES[1])  # Human chooses rock

    # Mock the computer's choice to always be paper
    async def mock_computer_choice():
        return const.CHOICES[2]  # Paper
    game.computer.strategy.choose = mock_computer_choice

    await game.play_round()

    assert game.round_number == 1
    assert game.scores[const.COMPUTER] == 1  # Comp should win
    captured = capsys.readouterr()
    assert "Computer wins the round!" in captured.out

@pytest.mark.asyncio
async def test_display_results(capsys):
    """Test that display results function outputs correct results."""
    game = Game(num_rounds=3)
    game.scores[const.HUMAN] = 2
    game.scores[const.COMPUTER] = 1
    game.scores[const.TIE] = 0
    game.round_number = 3
    
    # Capture output
    await game.display_results()
    
    captured = capsys.readouterr()
    
    assert "Final Score - You: 2, Computer: 1, Ties: 0" in captured.out

@pytest.mark.asyncio
async def test_play_game(capsys):
    """Test that the play_game function plays the right number of rounds."""
    # Test
    game = Game(num_rounds=2)
    async def mock_get_human_choice():
        return const.CHOICES[1]
    game.get_human_choice = mock_get_human_choice

    await game.play_game()

    assert game.round_number == 2
