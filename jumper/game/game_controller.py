from game.parachute import Parachute
from game.jumper import Jumper
from game.secret_word import SecretWord


class GameController():
    """Game Controller class represent the game controller."""

    def __init__(self):
        """Initialize a GameController object."""

        self._parachute = Parachute()
        self._jumper = Jumper()
        self._secret_word = SecretWord()

        self._game_over = False
        self._tries = []

    def start_game(self):
        """Start the game."""

        print("**************************")
        print("Welcome to the Jumper Game")
        print("**************************")

        self._secret_word.set_random_word()

        while not self._game_over:
            self._secret_word.display_letters()
            print()

            self._parachute.print()
            self._jumper.print()
            print()

            letter = self.ask_letter()

            if(letter):
                self._tries.append(letter)
                is_correct = self._secret_word.check_letter(letter)

                if is_correct:
                    self.check_word_guessed()

                else:
                    self._parachute.remove_part()

                    self.check_jumper_life()

            else:
                print(
                    "Invalid Option! This is not a letter or you have already tried this letter.")

            print()

        print("Thank you for play with us!")

    def ask_letter(self):
        """Ask a letter from the user."""

        letter = input("Guess a letter [a-z]: ").lower()

        if not letter.isalpha() or letter in self._tries:
            letter = ""

        return letter

    def check_word_guessed(self):
        """Check if the word was guessed."""

        if self._secret_word.is_word_guessed():
            self._game_over = True
            print("You win")

    def check_jumper_life(self):
        """Check if the jumper does not have more parachutes."""

        if self._parachute.remaining_parachute_parts() == 0:
            print()
            self._jumper.kill()
            self._jumper.print()
            print(f"You lose! The word was {self._secret_word.reveal_word()}")

            self._game_over = True
