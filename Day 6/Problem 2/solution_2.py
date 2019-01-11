import os
from string import ascii_uppercase

# INPUT_FILE = 'Day 6/Problem 1/input_example1.txt'
INPUT_FILE = 'Day 6/input_problem.txt'

with open(INPUT_FILE, 'r') as f:
    coordinates = f.read().splitlines()
    coordinates = [tuple(map(int, coord.split(', '))) for coord in coordinates]

named_coordinates = {
        ascii_uppercase[i//26] + ascii_uppercase[i % 26]: coord
        for i, coord in enumerate(coordinates)
    }

safe_locs = list()

MAX_ROW = 0
MAX_COL = 0

for coord in coordinates:
    if coord[0] > MAX_COL:
        MAX_COL = coord[0]
    if coord[1] > MAX_ROW:
        MAX_ROW = coord[1]

grid_size = max(MAX_ROW, MAX_COL) + 1

grid = {
    (col, row): '.' for col in range(grid_size) for row in range(grid_size)
}

for loc in grid:
    total_distance = 0
    for name, coord in named_coordinates.items():
        distance = abs(coord[0]-loc[0]) + abs(coord[1]-loc[1])
        total_distance += distance
    if total_distance < 10000:
        safe_locs.append(loc)

print(f'The size of the safe region is: {len(safe_locs)}.')