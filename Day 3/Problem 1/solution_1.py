INPUT_FILE = './Day 3/input_problem.txt'

claims = {}
unique_squares = set()
overlap_squares = set()

with open(INPUT_FILE, 'r') as f:
    claim_inputs = [line.strip('\n') for line in f.readlines()]

for claim in claim_inputs:
    pieces = claim.split()
    claim_id = pieces[0]
    left_edge, top_edge = pieces[2].strip(':').split(',')
    width, height = pieces[3].split('x')
    left_start = int(left_edge) + 1
    top_start = int(top_edge) + 1
    claims[claim_id] = set()
    for row in range(top_start, top_start+int(height)):
        for col in range(left_start, left_start+int(width)):
            square = f'{row},{col}'
            claims[claim_id].add(square)
            if square in unique_squares:
                overlap_squares.add(square)
            unique_squares.add(square)

print(f'Overlap length: {len(overlap_squares)}')