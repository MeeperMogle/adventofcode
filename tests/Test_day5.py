import unittest
from functions.day5 import jumps_required_to_escape_offsets
from functions.helpers import get_file_content_as_lines_int_list


class MyTestCase(unittest.TestCase):
    def test_first(self):
        # The message includes a list of the offsets for each jump.Jumps are relative: -1 moves to the previous
        # instruction, and 2 skips the next one. Start at the first instruction in the list. The goal is to follow
        # the jumps until one leads outside the list.
        #
        # In addition, these instructions are a little strange; after each jump, the offset of that instruction
        # increases by 1. So, if you come across an offset of 3, you would move three instructions forward, but
        # change it to a 4 for the next time it is encountered.
        #
        # For example, consider the following list of jump offsets:
        #
        # 0 3 0 1 -3
        #
        # Positive jumps("forward") move forward; negative jumps move backward.
        # The following steps would be taken before an exit is found:
        #
        # (0) 3  0  1  -3      before we have taken any steps.
        # (1) 3  0  1  -3      jump with offset 0 (don't jump at all). The instruction is then incremented to 1.
        #  2 (3) 0  1  -3      step forward because of the instruction we just modified. The first instruction is now 2
        #  2  4  0  1 (-3)     jump all the way to the end; leave a 4 behind.
        #  2 (4) 0  1  -2      go back to where we just were; increment -3 to -2.
        #  2  5  0  1  -2      jump 4 steps forward, escaping the maze.
        # In this example, the exit is reached in 5 steps.
        input_list = [0, 3, 0, 1, -3]
        self.assertEqual(jumps_required_to_escape_offsets(input_list), 5)

    def test_second(self):
        # Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1.
        # Otherwise, increase it by 1 as before.
        #
        # Using this rule with the above example, the process now takes 10 steps, and the offset values after finding
        # the exit are left as 2 3 2 3 -1.
        input_list = [0, 3, 0, 1, -3]
        self.assertEqual(jumps_required_to_escape_offsets(input_list, True), 10)

    def test_solutions(self):
        input_day5 = get_file_content_as_lines_int_list('day5.txt')
        self.assertEqual(jumps_required_to_escape_offsets(input_day5[:]), 391540)
        self.assertEqual(jumps_required_to_escape_offsets(input_day5[:], True), 30513679)
