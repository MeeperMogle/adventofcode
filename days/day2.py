from functions.day2 import calculate_spreadsheet_checksum_day2_1
from functions.helpers import get_tvs_file_content_as_int_spreadsheet

print('http://adventofcode.com/2017/day/2')

input_day2 = get_tvs_file_content_as_int_spreadsheet('day2.txt')

print('Part one:', calculate_spreadsheet_checksum_day2_1(input_day2))
