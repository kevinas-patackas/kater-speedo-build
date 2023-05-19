from gps import *
import time

running = True


def getPositionData(gps):
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        latitude = getattr(nx, 'lat', "unknown")
        longitude = getattr(nx, 'lon', "unknown")
        speed = getattr(nx, 'speed', "unknown")
        print("lon ", longitude)
        print("lat ", latitude)
        print("speed ", speed)
    if nx['class'] == 'ATT':
        heading = getattr(nx, 'heading', "unknown")
        mheading = getattr(nx, 'mheading', "unknown")
        print("heading ", heading)
        print("mheading ", mheading)


gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)

try:
    while running:
        getPositionData(gpsd)
        time.sleep(0.04)

except (KeyboardInterrupt):
    running = False
