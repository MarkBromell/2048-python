import cell
import random


class Board:
    __cell_width = 5

    def __init__(self, height=4, width=4):
        self._height = height
        self._width = width
        self._cells = []
        for _ in range(self.height):
            new_row = []
            for _ in range(self.width):
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

    def __eq__(self, other):
        if self.width != other.width or self.height != other.height:
            return False
        for row in range(self.height):
            for col in range(self.width):
                if self.get_cell(row, col) != other.get_cell(row, col):
                    return False
        return True

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def get_cell(self, x, y):
        return self._cells[x][y]

    def set_cell(self, x, y, value):
        self._cells[x][y].value = value

    def add_cell_random(self):
        # No ned to try add to a board that's full
        if self.is_full():
            return
        # Keep trying to add to the board until you hit an empty cell
        # (this is inefficient, but it works)
        while True:
            x = random.randint(0, self._height - 1)
            y = random.randint(0, self._width - 1)
            if self.get_cell(x, y).is_empty():
                self.set_cell(x, y, cell.starting_value())
                return x, y

    def is_full(self):
        for row in range(self._height):
            for col in range(self._width):
                if self._cells[row][col].is_empty():
                    return False
        return True

    @staticmethod
    def _str_cell(value):
        return '{:^5}│'.format(str(value))

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
