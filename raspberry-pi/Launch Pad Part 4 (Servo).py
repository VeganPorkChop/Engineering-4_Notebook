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

while True:
    if button_a.value == False:
        for x in range(10, -1 ,-1):
            if x > 0:
                print(x)
            if x == 0:
                print('LAUNCH')
                ledGreen.value = True
                servo1.angle = 180
                time.sleep(0.1)
                print('Countdown Finished!')
                time.sleep(5)
            ledRed.value = True
            time.sleep(0.5)
            ledRed.value = False
            time.sleep(0.5)
    else:
        servo1.angle = 0
        ledGreen.value = False
        print('Waiting For Button')