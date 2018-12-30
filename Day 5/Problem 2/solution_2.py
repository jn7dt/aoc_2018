import os
import string

# INPUT_TEXT = 'Day 5/Problem 1/input_example1.txt'
INPUT_TEXT = 'Day 5/input_problem.txt'

with open(INPUT_TEXT, 'r') as f:
    polymer = f.read().strip('\n')

def polymer_length(polymer, pairs):
    start_length = len(polymer)
    resulting_length = 0

    while resulting_length != start_length:
        start_length = len(polymer)
        for pair in pairs:
            polymer = polymer.replace(pair, '')
            resulting_length = len(polymer)
    
    return resulting_length

types = list(zip(string.ascii_lowercase, string.ascii_uppercase))
pairs = [char[0]+char[1] for char in types]
pairs += [chars[1]+chars[0] for chars in pairs]

shortest_length = None

for unit_type in types:
    test_polymer = polymer.replace(unit_type[0],'').replace(unit_type[1],'')
    test_length = polymer_length(test_polymer, pairs)
    if shortest_length is None or test_length < shortest_length:
        shortest_length = test_length

print(f'Shortest polymer length: {shortest_length}')