class Jumper:
    """Jumper class represent the jumper"""

    def __init__(self):
        """Initialize a Jumper object."""

        self._head = "  O"
        self._core = " /|\\"
        self._lower = " / \\"
        self._floor = "^^^^^"

    def kill(self):
        """Replace the head of the jumper to show that he is dead."""

        self._head = self._head.replace("O", "X")

    def print(self):
        """Show the jumper."""

        print(self._head)
        print(self._core)
        print(self._lower)
        print()
        print(self._floor)
