import board
import time
import digitalio

while True:
    for x in range(10, -1 ,-1):
        time.sleep(1)
        print(x)
        if x == 0:
            print('LAUNCH')