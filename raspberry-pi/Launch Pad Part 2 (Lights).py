import board
import time
import digitalio

ledRed = digitalio.DigitalInOut(board.GP0)
ledRed.direction = digitalio.Direction.OUTPUT
ledGreen = digitalio.DigitalInOut(board.GP1)
ledGreen.direction = digitalio.Direction.OUTPUT
count = 0

while True:
    for x in range(10, -1 ,-1):
        if count == 0:
            if x > 0:
                print(x)
            if x == 0:
                print('LAUNCH')
                ledGreen.value = True
                count = 1
            ledRed.value = True
            time.sleep(0.5)
            ledRed.value = False
            time.sleep(0.5)
        else:
            print('Countdown Finished')