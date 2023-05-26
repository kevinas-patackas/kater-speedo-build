import time
import Adafruit_ADS1x15
import json
import argparse

parser = argparse.ArgumentParser(description='Read ADC data.')
parser.add_argument('args', metavar='args', type=str,
                    help='JSON string with arguments')
args = parser.parse_args()

adc_args = json.loads(args.args)
sleep_time = adc_args.get('sleepTime', 0.5)
adc_address = int(adc_args.get('adcAddress', '0x48'), 16)
channel = adc_args.get('channel', 0)
deviation = adc_args.get('deviation', None)
BUSNUM = adc_args.get('busnum', 1)
GAIN = adc_args.get('gain', 1)

if deviation is not None:
    active_sleep_time = adc_args.get('activeSleepTime', 0.03)

adc = Adafruit_ADS1x15.ADS1115(address=adc_address, busnum=BUSNUM)

# initialize previous value
prev_value = adc.read_adc(channel, gain=GAIN)

# Main loop.
while True:
    value = adc.read_adc(channel, gain=GAIN)

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
