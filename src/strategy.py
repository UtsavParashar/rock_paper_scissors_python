import random
from abc import ABC, abstractmethod
from collections import defaultdict

import src.constants as const

class Strategy(ABC):
    """Abstract base class for defining computer player strategies."""

    @abstractmethod
    def choose(self, history):
        """Chooses an action based on the game history."""
        pass

    @abstractmethod
    def update_rewards(self, computer_choice, player_choice, history):
        """Updates strategy based on the outcome of the round."""
        pass

class CombinedStrategy(Strategy):
    """Combines RL, Markov Modeling for an adaptive Strategy."""

    def __init__(self, epsilon=0.1, learning_rate=0.1, markov_order=1, initial_exploration_rounds=10):
        """Initializes the strategy with learning parameters and data structures."""
        self.action_values = defaultdict(float)  # RL values for each action
        self.action_counts = defaultdict(int)    # Counts of each action chosen
        self.epsilon = epsilon                   # Exploration rate
        self.learning_rate = learning_rate      # Learning rate for RL
        self.markov_order = markov_order         # Order of Markov model
        self.markov_model = defaultdict(lambda: defaultdict(int))  # Markov model for transitions
        self.regrets = defaultdict(float)
        total_choices_count = len(const.CHOICES) - 1  # Exclude 'exit'
        initial_probability = 1 / total_choices_count
        self.action_probabilities = {choice: initial_probability for choice in const.CHOICES[1:]}
        self.initial_exploration_rounds = initial_exploration_rounds
        self.current_round = 0  # Track the current round

    def choose(self, history):
        """Chooses an action based on the game history, Markov model, and game theory."""
        self.current_round += 1
        
        if self.current_round <= self.initial_exploration_rounds:
            return random.choice(const.CHOICES[1:])

        # 1. Markov Model Prediction:
        predicted_move = self.predict_human_move(history)
        if predicted_move:
            best_action = self.counter_action(predicted_move)
            return best_action
        
        # 2. Reinforcement Learning fallback
        blended_values = {action: self.action_values[action] + self.regrets[action] for action in const.CHOICES[1:]}
        max_value = max(blended_values.values())
        normalized_values = {action: value / max_value if max_value != 0 else value for action,value in blended_values.items()}
        
        return max(normalized_values.keys(), key=lambda x: normalized_values[x])

    # Reinforcement Learning helper
    def update_rewards(self, computer_choice, player_choice, history):
        """Updates the strategy based on the outcome of the round."""
        reward = self.get_reward(computer_choice, player_choice)
        n = self.action_counts[computer_choice] + 1
        self.action_counts[computer_choice] = n
        value_estimate = self.action_values[computer_choice]
        new_value_estimate = value_estimate + (reward - value_estimate) / n
        self.action_values[computer_choice] = new_value_estimate

        for action in const.CHOICES[1:]:
            hypothetical_payoff = self.get_reward(action, player_choice)
            self.regrets[action] += hypothetical_payoff - reward

        if len(history) > 1: # To have at least 2 moves to compute transition
            last_action = history[-2]
            self.markov_model[last_action][player_choice] += 1 # Train markov model on what the *player* did

    # Reinforcement learning helper
    def get_reward(self, computer_choice, player_choice):
        """Calculates reward based on choices made."""
        if computer_choice == player_choice:
            return const.TIE_REWARD

        if ((computer_choice == const.CHOICES[1] and player_choice == const.CHOICES[3]) or
            (computer_choice == const.CHOICES[2] and player_choice == const.CHOICES[1]) or
            (computer_choice == const.CHOICES[3] and player_choice == const.CHOICES[2])):
            return const.WIN

        return const.LOSE

    # Markov helper
    def predict_human_move(self, history):
        """Predicts the human player's next move using the Markov model."""
        if len(history) < 1:  # Check if there is enough history to make a prediction
            return None
        
        last_move = history[-1]  # Get the last move made by the human player
        predicted_move = max(self.markov_model[last_move], key=self.markov_model[last_move].get, default=None)
        return predicted_move

    # Markov helper
    def counter_action(self, predicted_move):
        """Chooses an action to counter the predicted move."""
        if predicted_move == const.CHOICES[1]:  # Rock
            return const.CHOICES[2]  # Choose Paper
        elif predicted_move == const.CHOICES[2]:  # Paper
            return const.CHOICES[3]  # Choose Scissors
        elif predicted_move == const.CHOICES[3]:  # Scissors
            return const.CHOICES[1]  # Choose Rock
