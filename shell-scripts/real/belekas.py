import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()  # Create an instance of the ADS1015 ADC

GAIN = 16  # Set the ADC gain (options: 1, 2/3, 1, 2, 4, 8, 16)

while True:
    value = adc.read_adc(0, gain=GAIN)  # Read the ADC value from channel 0
    print(value)
    time.sleep(0.5)
