import random


class Cell:
    def __init__(self, value=0):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

    def increase_value(self):
        self._value *= 2

    def initialize_value(self):
        random_number = random.randint(1, 6)

        if random_number >= 1 or random_number <= 5:
            self._value = 2
        else:
            self._value = 4

    def can_combine(self, other):
        if self._value == other.get_value():
            return True
        else:
            return False
