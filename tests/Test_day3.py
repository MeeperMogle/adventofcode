import unittest

from functions.day3 import calculate_steps_needed
from functions.helpers import get_file_content_as_single_int

print('http://adventofcode.com/2017/day/3')


class MyTestCase(unittest.TestCase):
    def test_first(self):
        # Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up
        # while spiraling outward. For example, the first few squares are allocated like this:
        #
        # 17  16  15  14  13
        # 18   5   4   3  12
        # 19   6   1   2  11
        # 20   7   8   9  10
        # 21  22  23---> ...
        # While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1
        # (the location of the only access port for this memory system)
        # by programs that can only move up, down, left, or right. They always take the shortest path:
        # the Manhattan Distance between the location of the data and square 1.
        #
        # For example:
        #
        # Data from square 1 is carried 0 steps, since it's at the access port.
        # Data from square 12 is carried 3 steps, such as: down, left, left.
        # Data from square 23 is carried only 2 steps: up twice.
        # Data from square 1024 must be carried 31 steps.
        self.assertEqual(calculate_steps_needed(1), 0)
        self.assertEqual(calculate_steps_needed(12), 3)
        self.assertEqual(calculate_steps_needed(23), 2)
        self.assertEqual(calculate_steps_needed(1024), 31)

    def test_solutions(self):
        input_day3 = get_file_content_as_single_int('day3.txt')
        self.assertEqual(calculate_steps_needed(input_day3), 480)


if __name__ == '__main__':
    unittest.main()
