INPUT = 'Day 1\input_problem.txt'
STARTING_FREQUENCY = 0

with open(INPUT, 'r') as f:
    frequency_inputs = f.readlines()

frequency_changes = [float(frequency) for frequency in frequency_inputs]

resulting_frequency = STARTING_FREQUENCY + sum(frequency_changes)

print(f'Resulting frequency: {resulting_frequency}')