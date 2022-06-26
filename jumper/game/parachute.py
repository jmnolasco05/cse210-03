class Parachute:
    """Parachute class represent the parachute of the jumper"""

    def __init__(self):
        self._parachute = [
            " ___",
            "/___\\",
            "\\   /",
            " \ /"
        ]

    def remove_part(self):
        """Remove a parachute line of the list"""

        self._parachute.pop(0)

    def remaining_parachute_parts(self):
        """Get the remaining parachute parts count.

        Returns:
            int: parachute list length
        """
        return len(self._parachute)

    def print(self):
        """Show the parachute"""

        for part in self._parachute:
            print(part)
