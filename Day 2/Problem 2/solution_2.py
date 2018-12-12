from collections import Counter

# INPUT_FILE = './Day 2/Problem 2/input_example1.txt'
INPUT_FILE = './Day 2/input_problem.txt'

with open(INPUT_FILE, 'r') as f:
    box_ids = [box_id.strip('\n') for box_id in f.readlines()]

shared_letters = ''

for char in range(27):
    temp_ids = ['{}{}'.format(box_id[:char], box_id[char+1:]) for box_id in box_ids]
    id_count = Counter(temp_ids)
    most_common = id_count.most_common(1)
    if most_common[0][1] >= 2:
        shared_letters = most_common[0][0]

print(f'Shared letters: {shared_letters}')