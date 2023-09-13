import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

pwm_servo = pwmio.PWMOut(board.GP22, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
ledRed = digitalio.DigitalInOut(board.GP0)
ledRed.direction = digitalio.Direction.OUTPUT
ledGreen = digitalio.DigitalInOut(board.GP1)
ledGreen.direction = digitalio.Direction.OUTPUT
button_a = digitalio.DigitalInOut(board.GP15)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP
st = time.monotonic()
lt = 100000000000000000000
z = 0

while True:
    if button_a.value == False:
        for x in range(10, -1 ,-1):
            ct = time.monotonic()
            tp = ct-st
            if tp >= 1/60:
                z = 1
            if x <= 3 and z == 1:
                for y in range(0, 181, 1):
                    servo1.angle = y
            if x > 0:
                print(x)
            elif x == 0:
                print('LAUNCH')
                ledGreen.value = True
                print('Countdown Finished!')
            ledRed.value = True
            ct = time.monotonic()
            tt = ct + .5
            while ct < tt:
                ct = time.monotonic()
                print(ct)
            ct = time.monotonic()
            ledRed.value = False
            tt = ct + .5
            while ct < tt:
                ct = time.monotonic()
                print(ct)
    else:
        z = 0
        servo1.angle = 0
        ledGreen.value = False
        print('Waiting For Button')