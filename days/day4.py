from functions.day4 import passphrase_is_valid, passphrase_is_valid_no_anagrams
from functions.helpers import get_file_content_as_lines_list

print('http://adventofcode.com/2017/day/4')

input_day4 = get_file_content_as_lines_list('day4.txt')

valid_phrases_v1 = 0
valid_phrases_v2 = 0

for passphrase in input_day4:
    valid_phrases_v1 += 1 if passphrase_is_valid(passphrase) else 0
    valid_phrases_v2 += 1 if passphrase_is_valid_no_anagrams(passphrase) else 0

print('Part one:', valid_phrases_v1)
print('Part two:', valid_phrases_v2)
