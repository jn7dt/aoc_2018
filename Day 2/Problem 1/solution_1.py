from collections import Counter

INPUT_FILE = './Day 2/input_problem.txt'

with open(INPUT_FILE, 'r') as f:
    box_ids = f.readlines()

id_counts = {'2': 0, '3': 0}

for box_id in box_ids:
    box_id = box_id.strip('\n')
    counts = Counter(box_id)
    exactly_two = False
    exactly_three = False
    for char, count in counts.items():
        if count == 3:
            exactly_three = True
        elif count == 2:
            exactly_two = True
    
    id_counts['2'] += exactly_two
    id_counts['3'] += exactly_three

checksum = id_counts['2'] * id_counts['3']
print(f'Checksum: {checksum}')