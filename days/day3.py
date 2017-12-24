from functions.day3 import calculate_steps_needed
from functions.helpers import get_file_content_as_single_int

print('http://adventofcode.com/2017/day/3')

input_day3 = get_file_content_as_single_int('day3.txt')

print('Part one:', calculate_steps_needed(input_day3))
# print('Part two:', calculate_spreadsheet_checksum_day2_2(input_day3))
