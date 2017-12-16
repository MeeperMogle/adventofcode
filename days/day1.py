from functions.day1 import solve_captcha_day1_1, solve_captcha_shift
from functions.helpers import get_file_content_as_int_list

print('http://adventofcode.com/2017/day/1')

input_day1 = get_file_content_as_int_list('day1.txt')

print('Part one:', solve_captcha_day1_1(input_day1))
print('Part one, enhanced:', solve_captcha_shift(input_day1))

if solve_captcha_day1_1(input_day1) == solve_captcha_shift(input_day1):
    print('Part two:', solve_captcha_shift(input_day1, int(len(input_day1) / 2)))
else:
    print("Second function doesn't give expected result on long input...")
