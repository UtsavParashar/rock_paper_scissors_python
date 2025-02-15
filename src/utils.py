def get_valid_choice(prompt, valid_choices):
    """Prompts the user for input and validates it against a list of valid choices."""
    while True:
        choice = input(prompt).lower()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter one of: {', '.join(valid_choices)}")
