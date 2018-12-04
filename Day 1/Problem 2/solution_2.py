INPUT = 'Day 1\input_problem.txt'
STARTING_FREQUENCY = 0

with open(INPUT, 'r') as f:
    frequency_inputs = f.readlines()

frequency_changes = [float(frequency) for frequency in frequency_inputs]
frequencies_reached = {STARTING_FREQUENCY}

duplicate_reached = False
current_frequency = STARTING_FREQUENCY

while not duplicate_reached:
    for frequency_change in frequency_changes:
        current_frequency += frequency_change
        if current_frequency in frequencies_reached:
            duplicate_reached = True
            break
        else:
            frequencies_reached.add(current_frequency)

print(f'Duplicate frequency: {current_frequency}')