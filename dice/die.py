from random import randint


class Die:
    """a class for a single die"""

    def __init__(self, num_sides=6):
        """default to six sided die"""
        self.num_sides = num_sides

    def roll(self):
        """simulate roll"""
        return randint(1, self.num_sides)
