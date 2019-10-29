import random


class Cell:
    def __init__(self, value=0):
        self._value = value

    def __str__(self):
        return str(self._value)

    def __eq__(self, other):
        return self._value == other.value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def increase_value(self):
        self._value *= 2

    def can_combine(self, other):
        if self._value == other.value:
            return True
        else:
            return False

    def is_empty(self):
        return self._value == 0


def starting_value():
    random_number = random.randint(1, 6)
    if random_number >= 1 or random_number <= 5:
        return 2
    else:
        return 4
