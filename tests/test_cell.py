import unittest
import cell


class TestCell(unittest.TestCase):
    def test_str(self):
        my_cell = cell.Cell(2)
        self.assertEquals(str(my_cell), "2")

    def test_get_value(self):
        my_cell = cell.Cell(2)
        self.assertEquals(my_cell.get_value(), 2)

    def test_increase_value(self):
        my_cell = cell.Cell(4)
        my_cell.increase_value()
        self.assertEquals(my_cell.get_value(), 8)

    def test_initialize_value(self):
        my_cell = cell.Cell()
        my_cell.initialize_value()
        self.assertTrue(my_cell.get_value() == 2 or my_cell.get_value() == 4)

    def test_can_combine_invalid(self):
        cell1 = cell.Cell(2)
        cell2 = cell.Cell(4)
        self.assertFalse(cell1.can_combine(cell2))

    def test_can_combine_valid(self):
        cell1 = cell.Cell(4)
        cell2 = cell.Cell(4)
        self.assertTrue(cell1.can_combine(cell2))
