import board
import time
import digitalio
import pwmio
import simpleio
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
z = 0
cd = 0
bp = 0
ABORTER = 1
t = False
while True:
    if button_a.value == False and ABORTER == 1 and t == True:
        ABORTER = 0
        ct = time.monotonic()
        x = st - ct
        cd = 10 - x
        if cd <= 3:
            for y in range(0, 181, 1):
                servo1.angle = y
        if cd > 0:
            print(cd)
        if cd == 0:
            print('LAUNCH')
            ledGreen.value = True
            print('Countdown Finished!')
        if 0.5 >= st - (ct + 0.5*bp):
            bp = bp+ 1
            led = True
            if led == True:
                ledRed = False
                led = False
            ledRed = True
    elif button_a.value == False and ABORTER == 0:
        print("ABORT")
        ABORTER = 1
    else:
        z = 0
        servo1.angle = 0
        ledGreen.value = False
        print('Waiting For Button')