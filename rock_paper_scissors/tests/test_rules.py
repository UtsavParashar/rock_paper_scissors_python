import pytest
from src.rules import Rules
from src import constants as const

def test_determine_winner():
    """Test that determine_winner function returns the correct winner."""
    rules = Rules()
    
    assert rules.determine_winner(const.CHOICES[1], const.CHOICES[2]) == const.COMPUTER  # Rock vs Paper -> Computer wins
    assert rules.determine_winner(const.CHOICES[2], const.CHOICES[3]) == const.COMPUTER  # Paper vs Scissors -> Computer wins
    assert rules.determine_winner(const.CHOICES[3], const.CHOICES[1]) == const.HUMAN     # Scissors vs Rock -> Human wins
    assert rules.determine_winner(const.CHOICES[1], const.CHOICES[1]) == const.TIE       # Rock vs Rock -> Tie
