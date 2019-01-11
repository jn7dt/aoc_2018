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

coord_areas = {coord: 0 for coord in named_coordinates}

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
    shortest_distance = None
    closest_coord = None
    for name, coord in named_coordinates.items():
        distance = abs(coord[0]-loc[0]) + abs(coord[1]-loc[1])
        if shortest_distance is None or distance < shortest_distance:
            shortest_distance = distance
            closest_coord = name
        elif distance == shortest_distance:
            closest_coord = '.'
    grid[loc] = closest_coord
    if closest_coord != '.':
        coord_areas[closest_coord] += 1

TOP_EDGE = min([coord[1] for coord in coordinates])
RIGHT_EDGE = max([coord[0] for coord in coordinates])
BOTTOM_EDGE = max([coord[1] for coord in coordinates])
LEFT_EDGE = min([coord[0] for coord in coordinates])

edges = set()

for edge in range(grid_size):
    top_edge_coord = grid[(edge,0)]
    right_edge_coord = grid[(grid_size-1,edge)]
    bottom_edge_coord = grid[(edge,grid_size-1)]
    left_edge_coord = grid[(0,edge)]
    if top_edge_coord != '.':
        edges.add(top_edge_coord)
    if right_edge_coord != '.':
        edges.add(right_edge_coord)
    if bottom_edge_coord != '.':
        edges.add(bottom_edge_coord)
    if left_edge_coord != '.':
        edges.add(left_edge_coord)

for edge_coord in edges:
    del coord_areas[edge_coord]

largest_area = max(coord_areas, key=coord_areas.get)

print(f'The coordinate with the largest area is: {largest_area}',
    f'with a size of {coord_areas[largest_area]}.'
)

print(coord_areas)