import time
import Adafruit_ADS1x15
import json
import argparse

parser = argparse.ArgumentParser(description='Read ADC data.')
parser.add_argument('args', metavar='args', type=str,
                    help='JSON string with arguments')
args = parser.parse_args()

# READ JSON INPUT TO VALUES
adc_args = json.loads(args.args)
sleep_time = adc_args.get('sleepTime', 0.5)
adc_address = int(adc_args.get('adcAddress', '0x48'), 16)
channel = adc_args.get('channel', 0)
deviation = adc_args.get('deviation', None)
BUSNUM = adc_args.get('busnum', 1)
GAIN = adc_args.get('gain', 1)
range_map = adc_args['valueRangeMap']
range_map_sorted = {
    **range_map,
    "ranges": sorted(range_map["ranges"], key=lambda x: x["reading"]),
}

if deviation is not None:
    active_sleep_time = adc_args.get('activeSleepTime', 0.03)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.


# READ JSON INPUT TO VALUES
def find_value_by_range(reading):
    if range_map_sorted['limitToMinMax']:
        if range_map_sorted['min']['reading'] > reading:
            return round(range_map_sorted['min']['value'])
        if range_map_sorted['max']['reading'] < reading:
            return round(range_map_sorted['max']['value'])

    upper_range_index = -1
    for i in range(len(range_map_sorted["ranges"])):
        if range_map_sorted["ranges"][i]["reading"] > reading:
            upper_range_index = i
            break

    if upper_range_index == -1:
        upper_range = range_map_sorted["max"]
        lower_range = range_map_sorted["ranges"][-1] if len(
            range_map_sorted["ranges"]) > 0 else range_map_sorted["min"]
    else:
        upper_range = range_map_sorted["ranges"][upper_range_index]
        lower_range = range_map_sorted["ranges"][upper_range_index -
                                                 1] if upper_range_index > 0 else range_map_sorted["min"]

    value = (reading - lower_range["reading"]) / (upper_range["reading"] - lower_range["reading"]) * (
        upper_range["value"] - lower_range["value"]) + lower_range["value"]

    return round(value)


# START ADS READING
adc = Adafruit_ADS1x15.ADS1015(address=adc_address, busnum=BUSNUM)

# initialize previous value
prev_value = find_value_by_range(adc.read_adc(channel, gain=GAIN))

# Main loop.
while True:
    value = find_value_by_range(adc.read_adc(channel, gain=GAIN))

    # check if deviation is not None and value deviation is greater than the threshold
    if deviation is not None:
        if abs(value - prev_value) >= deviation:
            sleep_time = active_sleep_time
        else:
            sleep_time = adc_args.get('sleepTime', 0.5)

    # print the raw value
    print(value)

    # update the previous value
    prev_value = value

    time.sleep(sleep_time)


# import time
# import Adafruit_ADS1x15
# import json
# import argparse

# parser = argparse.ArgumentParser(description='Read ADC data.')
# parser.add_argument('args', metavar='args', type=str,
#                     help='JSON string with arguments')
# args = parser.parse_args()

# adc_args = json.loads(args.args)
# sleep_time = adc_args.get('sleepTime', 0.5)
# adc_address = int(adc_args.get('adcAddress', '0x48'), 16)
# channel = adc_args.get('channel', 0)
# deviation = adc_args.get('deviation', None)
# BUSNUM = adc_args.get('busnum', 1)
# GAIN = adc_args.get('gain', 1)

# if deviation is not None:
#     active_sleep_time = adc_args.get('activeSleepTime', 0.03)

# adc = Adafruit_ADS1x15.ADS1015(address=adc_address, busnum=BUSNUM)

# # initialize previous value
# prev_value = adc.read_adc(channel, gain=GAIN)

# # Main loop.
# while True:
#     value = adc.read_adc(channel, gain=GAIN)

#     # check if deviation is not None and value deviation is greater than the threshold
#     if deviation is not None:
#         if abs(value - prev_value) >= deviation:
#             sleep_time = active_sleep_time
#     else:
#         sleep_time = adc_args.get('sleepTime', 0.5)

#     # print the raw value
#     print(value)

#     # update the previous value
#     prev_value = value

#     time.sleep(sleep_time)
