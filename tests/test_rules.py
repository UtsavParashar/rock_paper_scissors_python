import pytest
from src.rules import Rules
from src import constants as const

def test_determine_winner():
    """Test that determine_winner function returns the correct winner."""
    rules = Rules()
    assert rules.determine_winner(const.CHOICES[1], const.CHOICES[2]) == const.COMPUTER  # Rock vs Paper -> Computer wins
    assert rules.determine_winner(const.CHOICES[2], const.CHOICES[3]) == const.COMPUTER  # Paper vs Scissors -> Computer wins
    assert rules.determine_winner(const.CHOICES[3], const.CHOICES[1]) == const.COMPUTER  # Scissors vs Rock -> Computer wins
    assert rules.determine_winner(const.CHOICES[2], const.CHOICES[1]) == const.HUMAN     # Paper vs Rock -> Human wins
    assert rules.determine_winner(const.CHOICES[3], const.CHOICES[2]) == const.HUMAN     # Scissors vs Paper -> Human wins
    assert rules.determine_winner(const.CHOICES[1], const.CHOICES[3]) == const.HUMAN     # Rock vs Scissors -> Human wins
    assert rules.determine_winner(const.CHOICES[1], const.CHOICES[1]) == const.TIE       # Rock vs Rock -> Tie
    assert rules.determine_winner(const.CHOICES[2], const.CHOICES[2]) == const.TIE       # Paper vs Paper -> Tie
    assert rules.determine_winner(const.CHOICES[3], const.CHOICES[3]) == const.TIE       # Scissors vs Scissors -> Tie
    
if __name__ == '__main__':
    test_determine_winner()

