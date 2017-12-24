from functions.day5 import jumps_required_to_escape_offsets
from functions.helpers import get_file_content_as_lines_int_list

print('http://adventofcode.com/2017/day/5')

input_day5 = get_file_content_as_lines_int_list('day5.txt')

print('Part one:', jumps_required_to_escape_offsets(input_day5))
