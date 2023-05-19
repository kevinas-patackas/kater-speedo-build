import random
import argparse
import json
import time

parser = argparse.ArgumentParser(description='Read ADC data.')
parser.add_argument('args', metavar='args', type=str,
                    help='JSON string with arguments')
args = parser.parse_args()

adc_args = json.loads(args.args)
range_map = adc_args['valueRangeMap']
sleep_time = adc_args.get('sleepTime', 0.5)
active_sleep_time = adc_args.get('activeSleepTime', 0.03)

min_value = range_map['min']['value']
max_value = range_map['max']['value']

mocked_reading = []

for value_in_range in list(range(1)):
    random_number = random.randint(5, 10)
    for rand_ in list(range(random_number)):
        mocked_reading.append(min_value)

for value_in_range in list(range(min_value, round(((max_value-min_value)/2)+min_value))):
    random_number = random.randint(1, 1)
    for rand_ in list(range(random_number)):
        mocked_reading.append(value_in_range)

for value_in_range in list(range(1)):
    random_number = random.randint(10, 15)
    for rand_ in list(range(random_number)):
        mocked_reading.append(round(((max_value-min_value)/2)+min_value))

for value_in_range in list(range(round(((max_value-min_value)/2)+min_value), max_value + 1)):
    random_number = random.randint(1, 1)
    for rand_ in list(range(random_number)):
        mocked_reading.append(value_in_range)

for value_in_range in list(range(1)):
    random_number = random.randint(5, 10)
    for rand_ in list(range(random_number)):
        mocked_reading.append(max_value)

reverse_mocked_reading = list(reversed(mocked_reading))
mocked_reading = mocked_reading + reverse_mocked_reading

mocked_index = -1


def get_next_reading():
    global mocked_index
    mocked_index += 1
    if mocked_index >= len(mocked_reading):
        mocked_index = 0
    return mocked_reading[mocked_index]


prev_value = get_next_reading()

while True:
    value = get_next_reading()

    # check if deviation is not None and value deviation is greater than the threshold
    if abs(value - prev_value) >= 1:
        sleep_time = active_sleep_time
    else:
        sleep_time = adc_args.get('sleepTime', 0.5)

    # print the raw value
    print(value)

    # update the previous value
    prev_value = value

    time.sleep(sleep_time)
