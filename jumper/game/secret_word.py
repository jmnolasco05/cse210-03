import random


class SecretWord:
    """Secret Word class represent the random secret word and the guessed letters"""

    def __init__(self):
        """Initialize a SecretWord Object"""

        self._words = [
            "algorithm",
            "argument",
            "array",
            "bug",
            "class",
            "comment",
            "constant",
            "function",
            "loop",
            "object",
            "parameter",
            "return",
            "type",
            "variable"
        ]

        self._secret_word = ""
        self._displayed_letters = []

    def set_random_word(self):
        """Set the random word for the game."""

        self._secret_word = random.choice(self._words)

        for i in range(len(self._secret_word)):
            self._displayed_letters.append("_")

    def display_letters(self):
        """Show the guessed letters ('_' for the not guessed)."""

        for letter in self._displayed_letters:
            print(letter, end="")
        print()

    def reveal_word(self):
        """Show the secret word."""

        print(self._secret_word)

    def check_letter(self, guess):
        """Check if the user guess a letter.

        Args:
            guess (str): The letter that the user thinks is in the secret word.

        Returns:
            bool: Indicate if the guess is correct or incorrect.
        """

        indices = [index for index, letter in enumerate(
            self._secret_word) if letter == guess]

        is_correct = len(indices) > 0

        if(is_correct):
            for i in indices:
                self._displayed_letters[i] = guess

        return is_correct

    def is_word_guessed(self):
        """Check if word is guessed.

        Returns:
            bool: Indicate if the word was guessed.
        """
        return self._displayed_letters.count("_") == 0
