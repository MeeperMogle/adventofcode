import unittest
from functions.day1 import solve_captcha_day1_1


class MyTestCase(unittest.TestCase):
    def test_first(self):
        # 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
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


if __name__ == '__main__':
    unittest.main()
