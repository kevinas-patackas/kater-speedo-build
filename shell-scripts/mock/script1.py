running = True

print("jobanas greitis blet")


speedMock = [
    0, 1, 3, 5, 6, 7, 9, 10, 12, 14, 16, 18, 19, 21, 22, 24, 26, 27, 28, 29, 30,
    32, 34, 36, 38, 40, 41, 42, 44, 46, 47, 49, 50, 52, 53, 55, 57, 58, 60, 62,
    63, 65, 66, 68, 70, 72, 73, 74, 75, 77, 78, 80, 81, 82, 84, 85, 87, 89, 91,
    92, 94, 95, 97, 99, 100, 101, 103, 105, 107, 109, 109, 107, 105, 103, 101,
    100, 99, 97, 95, 94, 92, 91, 89, 87, 85, 84, 82, 81, 80, 78, 77, 75, 74, 73,
    72, 70, 68, 66, 65, 63, 62, 60, 58, 57, 55, 53, 52, 50, 49, 47, 46, 44, 42,
    41, 40, 38, 36, 34, 32, 30, 29, 28, 27, 26, 24, 22, 21, 19, 18, 16, 14, 12,
    10, 9, 7, 6, 5, 3, 1, 0, 0,
]


def getPositionData():
    for x in speedMock:
        print("speed ", x)


try:
    while running:
        getPositionData()

except (KeyboardInterrupt):
    running = False
