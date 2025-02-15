import pytest
from src.player import Player
from src import constants as const

def test_player_initialization():
    """Test that a player initializes with the correct attributes."""
    player = Player(const.HUMAN)
    assert player.name == const.HUMAN
    assert player.choice is None
    assert player.history == []

def test_player_choose():
    """Test that a player can choose a valid action."""
    player = Player(const.HUMAN)
    player.choose(const.CHOICES[1])  # Choose rock
    assert player.choice == const.CHOICES[1]

def test_player_invalid_choice():
    """Test that choosing an invalid action raises an error."""
    player = Player(const.HUMAN)
    
    with pytest.raises(ValueError):
        player.choose("invalid_choice")

def test_update_history():
    """Test that the human player keeps track of the game."""
    player = Player(const.HUMAN)
    player.update_history(const.CHOICES[1])
    assert player.history == [const.CHOICES[1]]
