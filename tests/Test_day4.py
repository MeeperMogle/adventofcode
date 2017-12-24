import unittest
from functions.day4 import passphrase_is_valid, passphrase_is_valid_no_anagrams
from functions.helpers import get_file_content_as_lines_list


class MyTestCase(unittest.TestCase):
    def test_first(self):
        # A new system policy has been put in place that requires all accounts to use a passphrase instead of simply
        # a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.
        # To ensure security, a valid passphrase must contain no duplicate words.
        #
        # For example:
        #
        # aa bb cc dd ee is valid.
        # aa bb cc dd aa is not valid - the word aa appears more than once.
        # aa bb cc dd aaa is valid - aa and aaa count as different words.
        self.assertEqual(passphrase_is_valid('aa bb cc dd ee'), True)
        self.assertEqual(passphrase_is_valid('aa bb cc dd aa'), False)
        self.assertEqual(passphrase_is_valid('aa bb cc dd aaa'), True)

    def test_solutions(self):
        input_day4 = get_file_content_as_lines_list('day4.txt')

        valid_phrases_v1 = 0
        valid_phrases_v2 = 0

        for passphrase in input_day4:
            valid_phrases_v1 += 1 if passphrase_is_valid(passphrase) else 0
            valid_phrases_v2 += 1 if passphrase_is_valid_no_anagrams(passphrase) else 0

        print('Part one:', valid_phrases_v1)
        print('Part two:', valid_phrases_v2)

        self.assertEqual(valid_phrases_v1, 325)
        self.assertEqual(valid_phrases_v2, 119)


if __name__ == '__main__':
    unittest.main()
