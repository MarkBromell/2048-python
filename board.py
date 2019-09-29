import cell
import random


class Board:
    __cell_width = 5

    def __init__(self, height=4, width=4):
        self._height = height
        self._width = width
        self._cells = []

        for _ in range(self._height):
            new_row = []
            for _ in range(self._width):
                new_row.append(cell.Cell(0))
            self._cells.append(new_row)

    def __str__(self):
        string = self._top_border()

        for row in range(self._height):
            string += '│'
            for col in range(self._width):
                string += self._str_cell(self._cells[row][col])

            string += '\n'
            if row != self._height - 1:
                string += self._middle_border()

        string += self._bottom_border()
        return string

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def add_cell_random(self):
        if self.is_full():
            return

        while True:
            random_row = random.randint(0, self._height - 1)
            random_col = random.randint(0, self._width - 1)

            if self._cells[random_row][random_col].is_empty():
                new_cell = cell.Cell()
                new_cell.initialize_value()
                self._cells[random_row][random_col] = new_cell
                return (random_row, random_col)

    def is_full(self):
        for row in range(self._height):
            for col in range(self._width):
                if self._cells[row][col].is_empty():
                    return False
        return True

    # region functions for drawing the board
    def _str_cell(self, value):
        return ('{:^5}│').format(str(value))

    def _top_border(self):
        string = '┌'

        for _ in range(self._width - 1):
            string += ('─' * self.__cell_width) + '┬'
        string += ('─' * self.__cell_width) + '┐\n'

        return string

    def _middle_border(self):
        string = '├'

        for _ in range(self._width - 1):
            string += ('─' * self.__cell_width) + '┼'
        string += ('─' * self.__cell_width) + '┤\n'

        return string

    def _bottom_border(self):
        string = '└'

        for _ in range(self._width - 1):
            string += ('─' * self.__cell_width) + '┴'
        string += ('─' * self.__cell_width) + '┘\n'

        return string
    # endregion
