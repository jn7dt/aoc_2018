import os
import string

# INPUT_TEXT = 'Day 5/Problem 1/input_example1.txt'
INPUT_TEXT = 'Day 5/input_problem.txt'

with open(INPUT_TEXT, 'r') as f:
    polymer = f.read().strip('\n')

pairs = [char[0]+char[1] for char in zip(string.ascii_lowercase, string.ascii_uppercase)]
pairs += [chars[1]+chars[0] for chars in pairs]
start_length = len(polymer)
resulting_length = 0

while resulting_length != start_length:
    start_length = len(polymer)
    for pair in pairs:
        polymer = polymer.replace(pair, '')
        resulting_length = len(polymer)

print(f'Remaining units: {resulting_length}')