import board
import time
import digitalio

ledRed = digitalio.DigitalInOut(board.GP0)
ledRed.direction = digitalio.Direction.OUTPUT
ledGreen = digitalio.DigitalInOut(board.GP1)
ledGreen.direction = digitalio.Direction.OUTPUT
button_a = digitalio.DigitalInOut(board.GP15) # at GP15 because button interfeared with leds, refrence pico pinmap
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP        # requires only two wires one to ground and the other to pin, prevents excess wires. Definition of, "fix it in code".

while True:
    if button_a.value == True:
        time.sleep(0.1)# debounce
        while button_a.value == false:
            for x in range(10, -1 ,-1):
                if x > 0:
                    print(x)
                if x == 0:
                    print('LAUNCH')
                    ledGreen.value = True
                    time.sleep(0.1)
                    print('Countdown Finished!')
                    time.sleep(5)
                ledRed.value = True
                time.sleep(0.5)
                ledRed.value = False
                time.sleep(0.5)
        print('ABORT')# code accurs when button is true
        quit() # quits script
        
    else:
        ledGreen.value = False
        print('Waiting For Button')
