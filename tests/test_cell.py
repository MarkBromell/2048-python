import unittest
import cell


class TestCell(unittest.TestCase):
    def test_starting_value(self):
        my_cell = cell.Cell()
        my_cell.value = cell.starting_value()
        self.assertTrue(my_cell.value == 2 or my_cell.value == 4)

    def test_str(self):
        my_cell = cell.Cell(2)
        self.assertEqual(str(my_cell), "2")

    def test_eq(self):
        cell1 = cell.Cell(4)
        cell2 = cell.Cell(4)
        self.assertTrue(cell1 == cell2)

    def test_not_eq(self):
        cell1 = cell.Cell(4)
        cell2 = cell.Cell(2)
        self.assertTrue(cell1 != cell2)

    def test_value(self):
        my_cell = cell.Cell(2)
        self.assertEqual(my_cell.value, 2)

    def test_increase_value(self):
        my_cell = cell.Cell(4)
        my_cell.increase_value()
        self.assertEqual(my_cell.value, 8)

    def test_can_combine_invalid(self):
        cell1 = cell.Cell(2)
        cell2 = cell.Cell(4)
        self.assertFalse(cell1.can_combine(cell2))

    def test_can_combine_valid(self):
        cell1 = cell.Cell(4)
        cell2 = cell.Cell(4)
        self.assertTrue(cell1.can_combine(cell2))

    def test_is_empty_true(self):
        my_cell = cell.Cell()
        self.assertTrue(my_cell.is_empty())

    def test_is_empty_false(self):
        my_cell = cell.Cell(2)
        self.assertFalse(my_cell.is_empty())
