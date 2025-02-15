import pytest
from unittest.mock import patch
from src.utils import get_valid_choice

@patch("builtins.input", return_value="rock")
def test_get_valid_choice_valid_input(mock_input):
    """Test valid input returns correct value."""
    valid_choices = ["rock", "paper", "scissors"]
    result = get_valid_choice("Enter your choice: ", valid_choices)
    assert result == "rock"

@patch("builtins.input", side_effect=["invalid", "paper"])
def test_get_valid_choice_invalid_then_valid(mock_input):
    """Test invalid input followed by valid input."""
    valid_choices = ["rock", "paper", "scissors"]
    result = get_valid_choice("Enter your choice: ", valid_choices)
    assert result == "paper"