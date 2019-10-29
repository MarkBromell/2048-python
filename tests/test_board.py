import unittest
import board
import cell


class TestBoard(unittest.TestCase):
    def test_str(self):
        my_board = board.Board(4, 4)
        string = (
            '┌─────┬─────┬─────┬─────┐\n'
            '│  0  │  0  │  0  │  0  │\n'
            '├─────┼─────┼─────┼─────┤\n'
            '│  0  │  0  │  0  │  0  │\n'
            '├─────┼─────┼─────┼─────┤\n'
            '│  0  │  0  │  0  │  0  │\n'
            '├─────┼─────┼─────┼─────┤\n'
            '│  0  │  0  │  0  │  0  │\n'
            '└─────┴─────┴─────┴─────┘\n'
        )
        self.assertEqual(str(my_board), string)

    def test_eq(self):
        board1 = board.Board(4, 4)
        board2 = board.Board(4, 4)
        self.assertTrue(board1 == board2)

    def test_not_eq(self):
        board1 = board.Board(4, 4)
        board2 = board.Board(4, 4)
        board2.set_cell(0, 0, 2)
        self.assertTrue(board1 != board2)

    def test_height(self):
        my_board = board.Board(4, 3)
        self.assertEqual(my_board.height, 4)

    def test_width(self):
        my_board = board.Board(3, 4)
        self.assertEqual(my_board.width, 4)

    def test_get_cell(self):
        my_board = board.Board(4, 4)
        self.assertEqual(my_board.get_cell(0, 0), cell.Cell(0))

    def test_setitem(self):
        my_board = board.Board(4, 4)
        my_board.set_cell(0, 0, 2)
        self.assertEqual(my_board.get_cell(0, 0), cell.Cell(2))

    def test_add_cell_random(self):
        my_board = board.Board(4, 4)
        location = my_board.add_cell_random()
        self.assertTrue(my_board.get_cell(location[0], location[1]).value != 0)

    def test_is_full_true(self):
        my_board = board.Board(4, 4)
        self.assertFalse(my_board.is_full())

    def test_is_full_false(self):
        my_board = board.Board(4, 4)
        my_board._cells[0][0] = cell.Cell(2)
        self.assertFalse(my_board.is_full())

    def test_str_cell(self):
        my_board = board.Board(4, 4)
        string = '  0  │'
        self.assertEqual(my_board._str_cell(0), string)

    def test_top_border(self):
        my_board = board.Board(4, 4)
        string = '┌─────┬─────┬─────┬─────┐\n'
        self.assertEqual(my_board._top_border(), string)

    def test_middle_border(self):
        my_board = board.Board(4, 4)
        string = '├─────┼─────┼─────┼─────┤\n'
        self.assertEqual(my_board._middle_border(), string)

    def test_bottom_border(self):
        my_board = board.Board(4, 4)
        string = '└─────┴─────┴─────┴─────┘\n'
        self.assertEqual(my_board._bottom_border(), string)
