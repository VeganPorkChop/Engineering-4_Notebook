import board                                   
import time
import digitalio
import pwmio
from adafruit_motor import servo # import from 8x.x package on adafruit website

pwm_servo = pwmio.PWMOut(board.GP22, duty_cycle=2 ** 15, frequency=50) # servo setup PWM PIN
redLED = digitalio.DigitalInOut(board.GP0) 
greenLED = digitalio.DigitalInOut(board.GP1)
button = digitalio.DigitalInOut(board.GP15)
redLED.direction = digitalio.Direction.OUTPUT
greenLED.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500) # Servo PULSE SIZE

servo1.angle = 0 # angle of servo
count = 0                        

while True:
    print('waiting for button')
    if button.value == False:
        count = 10
    while count > 3:                               
        print(count)
        redLED.value = True   
        count = count - 1
        time.sleep(.5)
        redLED.value = False
        time.sleep(.5)
    while count > 0 & count <= 3:
        print(count)
        redLED.value = True
        count = count - 1
        for x in range(10):
            servo1.angle = servo1.angle + 3
            time.sleep(.05)
        redLED.value = False
        for x in range(10):
            servo1.angle = servo1.angle + 3
            time.sleep(.05)
        if count == 0:                              
            print("launch")
            greenLED.value = True
            servo1.angle = 180
            time.sleep(5)