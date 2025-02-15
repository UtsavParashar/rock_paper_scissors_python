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
    """Combines RL, Markov Modeling, and Game Theory for an adaptive AI."""

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

        # 2. Game Theory:
        human_probs = self.estimate_human_probs(history)
        best_action_gt = self.game_theory_action(human_probs)
        
        # 3. Reinforcement Learning fallback
        blended_values = {action: self.action_values[action] + self.regrets[action] for action in const.CHOICES[1:]}
        max_value = max(blended_values.values())
        normalized_values = {action: value / max_value if max_value != 0 else value for action,value in blended_values.items()}
        
        return max(normalized_values.keys(), key=lambda x: normalized_values[x])

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

    def get_reward(self, computer_choice, player_choice):
        """Calculates reward based on choices made."""
        if computer_choice == player_choice:
            return const.TIE_REWARD

        if ((computer_choice == const.CHOICES[1] and player_choice == const.CHOICES[3]) or
            (computer_choice == const.CHOICES[2] and player_choice == const.CHOICES[1]) or
            (computer_choice == const.CHOICES[3] and player_choice == const.CHOICES[2])):
            return const.WIN

        return const.LOSE

    def predict_human_move(self, history):
        """Predicts the human player's next move using the Markov model."""
        if len(history) < 1:  # Check if there is enough history to make a prediction
            return None
        
        last_move = history[-1]  # Get the last move made by the human player
        predicted_move = max(self.markov_model[last_move], key=self.markov_model[last_move].get, default=None)
        return predicted_move

    def counter_action(self, predicted_move):
        """Chooses an action to counter the predicted move."""
        if predicted_move == const.CHOICES[1]:  # Rock
            return const.CHOICES[2]  # Choose Paper
        elif predicted_move == const.CHOICES[2]:  # Paper
            return const.CHOICES[3]  # Choose Scissors
        elif predicted_move == const.CHOICES[3]:  # Scissors
            return const.CHOICES[1]  # Choose Rock

    def estimate_human_probs(self, history):
        """Estimate probabilities for the human to choose rock, paper, or scissors."""
        rock_count = history.count(const.CHOICES[1])
        paper_count = history.count(const.CHOICES[2])
        scissors_count = history.count(const.CHOICES[3])

        total_moves = len(history)

        if total_moves == 0:
            return {const.CHOICES[1]: 1/3, const.CHOICES[2]: 1/3, const.CHOICES[3]: 1/3}

        return {
            const.CHOICES[1]: rock_count / total_moves,
            const.CHOICES[2]: paper_count / total_moves,
            const.CHOICES[3]: scissors_count / total_moves
        }

    def game_theory_action(self, human_probs):
        """Determines the best response based on human move probabilities."""
        payoff_matrix = {
            const.CHOICES[1]: {  # Rock
                const.CHOICES[1]: 0, const.CHOICES[2]: -1, const.CHOICES[3]: 1
            },
            const.CHOICES[2]: {  # Paper
                const.CHOICES[1]: 1, const.CHOICES[2]: 0, const.CHOICES[3]: -1
            },
            const.CHOICES[3]: {  # Scissors
                const.CHOICES[1]: -1, const.CHOICES[2]: 1, const.CHOICES[3]: 0
            }
        }

        expected_values = {}
        for my_action in const.CHOICES[1:]:
            expected_value = sum(
                payoff_matrix[my_action][opponent_action] * human_probs.get(opponent_action, 0)
                for opponent_action in const.CHOICES[1:]
            )
            expected_values[my_action] = expected_value
        
        best_action = max(expected_values, key=expected_values.get)
        return best_action
