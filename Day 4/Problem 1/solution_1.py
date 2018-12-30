import os
import re

INPUT_TEXT = 'Day 4/Problem 1/input_example1.txt'
# INPUT_TEXT = 'Day 4/input_problem.txt'
MAX_SLEEP = 0
MAX_MINUTE = None
MAX_GUARD = None

def get_minute(record):
    return record[15:17]

def get_hour(record):
    return record[12:14]

with open(INPUT_TEXT, 'r') as f:
    records = sorted([line.strip('\n') for line in f],
        key=lambda l: l[1:17]
    )

shift_start = re.compile(r'Guard #\d+ begins shift')
shift_sleep = re.compile(r'falls asleep')
shift_wake = re.compile(r'wakes up')

current_guard = None
start_minute = None
sleep_start = None
sleep_end = None

guards = dict()

for record in records:
    if shift_start.search(record):
        current_guard = re.findall(r'#\d+', record)[0]
        start_minute = get_minute(record) if get_hour(record) == '23' else '00'
    if shift_sleep.search(record):
        sleep_start = get_minute(record)
    if shift_wake.search(record):
        sleep_end = get_minute(record)
        if not current_guard in guards:
            guards[current_guard] = dict()
        for minute in range(int(sleep_start), int(sleep_end)):
            if not minute in guards[current_guard]:
                guards[current_guard][minute] = 1
            else:
                guards[current_guard][minute] += 1
            # if guards[current_guard][minute] > MAX_SLEEP:
            #     MAX_SLEEP = guards[current_guard][minute]
            #     MAX_MINUTE = minute
            #     MAX_GUARD = current_guard

for guard, minutes in guards.items():
    total_sleep = sum([sleep for minute, sleep in minutes.items()])
    if total_sleep > MAX_SLEEP:
        MAX_SLEEP = total_sleep
        MAX_GUARD = guard
        for minute, sleep in minutes.items():
            if MAX_MINUTE is None or sleep > minutes[MAX_MINUTE]:
                MAX_MINUTE = minute

multiplier = int(MAX_MINUTE) * int(MAX_GUARD[1:])
print(f'Minute: {MAX_MINUTE}\nID: {MAX_GUARD}\nAnswer: {multiplier}')