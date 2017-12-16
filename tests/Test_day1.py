import unittest
from functions.day1 import solve_captcha_day1_1, solve_captcha_shift
from functions.helpers import get_file_content_as_int_list


class MyTestCase(unittest.TestCase):
    def test_first(self):
        # 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2)
        #   matches the fourth digit.
        # 1111 produces 4 because each digit (all 1) matches the next.
        # 1234 produces 0 because no digit matches the next.
        # 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

        example1 = [1, 1, 2, 2]
        example2 = [1, 1, 1, 1]
        example3 = [1, 2, 3, 4]
        example4 = [9, 1, 2, 1, 2, 1, 2, 9]

        self.assertEqual(solve_captcha_day1_1(example1), 3)
        self.assertEqual(solve_captcha_day1_1(example2), 4)
        self.assertEqual(solve_captcha_day1_1(example3), 0)
        self.assertEqual(solve_captcha_day1_1(example4), 9)

    def test_full(self):
        # 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2)
        #   matches the fourth digit.
        # 1111 produces 4 because each digit (all 1) matches the next.
        # 1234 produces 0 because no digit matches the next.
        # 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
        example1 = [1, 1, 2, 2]
        example2 = [1, 1, 1, 1]
        example3 = [1, 2, 3, 4]
        example4 = [9, 1, 2, 1, 2, 1, 2, 9]

        self.assertEqual(solve_captcha_shift(example1), solve_captcha_day1_1(example1))
        self.assertEqual(solve_captcha_shift(example2), solve_captcha_day1_1(example2))
        self.assertEqual(solve_captcha_shift(example3), solve_captcha_day1_1(example3))
        self.assertEqual(solve_captcha_shift(example4), solve_captcha_day1_1(example4))

        # 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
        # 1221 produces 0, because every comparison is between a 1 and a 2.
        # 123425 produces 4, because both 2s match each other, but no other digit has a match.
        # 123123 produces 12.
        # 12131415 produces 4.
        example1 = [1, 2, 1, 2]
        example2 = [1, 2, 2, 1]
        example3 = [1, 2, 3, 4, 2, 5]
        example4 = [1, 2, 3, 1, 2, 3]
        example5 = [1, 2, 1, 3, 1, 4, 1, 5]

        self.assertEqual(solve_captcha_shift(example1, int(len(example1) / 2)), 6)
        self.assertEqual(solve_captcha_shift(example2, int(len(example2) / 2)), 0)
        self.assertEqual(solve_captcha_shift(example3, int(len(example3) / 2)), 4)
        self.assertEqual(solve_captcha_shift(example4, int(len(example4) / 2)), 12)
        self.assertEqual(solve_captcha_shift(example5, int(len(example5) / 2)), 4)

    def test_solutions(self):
        input_day1 = get_file_content_as_int_list('day1.txt')
        self.assertEqual(solve_captcha_day1_1(input_day1), 1144)
        self.assertEqual(solve_captcha_shift(input_day1), 1144)
        self.assertEqual(solve_captcha_shift(input_day1, int(len(input_day1) / 2)), 1194)

if __name__ == '__main__':
    unittest.main()
