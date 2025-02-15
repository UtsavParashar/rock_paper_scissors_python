import pytest
from src.strategy import CombinedStrategy
from src import constants as const

def test_choose_action():
    """Test that choose method selects an action based on history."""
    strategy = CombinedStrategy()
    history = [const.CHOICES[1], const.CHOICES[2]]

    # Should be one of rock, paper, or scissors
    action = strategy.choose(history)
    
    assert action in const.CHOICES[1:]

def test_update_rewards():
    """Test that update_rewards correctly updates values based on outcomes."""
    strategy = CombinedStrategy()
    
    history = [const.CHOICES[1], const.CHOICES[2]]
    strategy.update_rewards(const.CHOICES[1], const.CHOICES[2], history)
    
    assert strategy.action_counts[const.CHOICES[1]] == 1
