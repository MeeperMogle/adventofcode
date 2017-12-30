from functions.day6 import steps_until_earlier_state_reached
from functions.helpers import get_file_content_as_string

print('http://adventofcode.com/2017/day/6')

input_day6 = list(map(lambda c: int(c), get_file_content_as_string('day6.txt').split('\t')))

print('Part one:', steps_until_earlier_state_reached(input_day6[:]))
#print('Part two:', steps_until_earlier_state_reached(input_day6[:]))
