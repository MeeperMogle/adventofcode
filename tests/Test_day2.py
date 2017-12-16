import unittest
from functions.day2 import calculate_spreadsheet_checksum_day2_1
from functions.helpers import get_tvs_file_content_as_int_spreadsheet


class MyTestCase(unittest.TestCase):
    def test_first(self):
        # To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's
        # checksum. For each row, determine the difference between the largest value and the smallest value;
        # the checksum is the sum of all of these differences.
        # For example, given the following spreadsheet:
        #
        # 5 1 9 5
        # 7 5 3
        # 2 4 6 8
        # The first row's largest and smallest values are 9 and 1, and their difference is 8.
        # The second row's largest and smallest values are 7 and 3, and their difference is 4.
        # The third row's difference is 6.
        # In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

        spreadsheet = (
            (5, 1, 9, 5),
            (7, 5, 3),
            (2, 4, 6, 8)
        )

        self.assertEqual(calculate_spreadsheet_checksum_day2_1(spreadsheet), 18)

    def test_solutions(self):
        input_day2 = get_tvs_file_content_as_int_spreadsheet('day2.txt')
        self.assertEqual(calculate_spreadsheet_checksum_day2_1(input_day2), 37923)


if __name__ == '__main__':
    unittest.main()
