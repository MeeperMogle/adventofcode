from functions.day4 import passphrase_is_valid
from functions.helpers import get_file_content_as_lines_list

print('http://adventofcode.com/2017/day/4')

input_day4 = get_file_content_as_lines_list('day4.txt')

valid_phrases = 0

for passphrase in input_day4:
    valid_phrases += 1 if passphrase_is_valid(passphrase) else 0

print('Part one:', valid_phrases)
# print('Part two:', calculate_spreadsheet_checksum_day2_2(input_day3))
