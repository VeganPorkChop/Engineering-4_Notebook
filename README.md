# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Raspberry_Pi_Launch Pad part 1](#Launch_Pad_Part_1)
* [Raspberry_Pi_Launch Pad part 2](#Launch_Pad_Part_2_(Lights))
* [Raspberry_Pi_Launch Pad part 3](#Launch_Pad_Part_3_(Button))
* [Raspberry_Pi_Launch Pad part 4](#Launch_Pad_Part_4_(Servo))
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

### Test Link

[Hyperlink text](http://www.google.com)      

### Test Image

![Picture Name Here](https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/1f06f40f-1454-425c-afcd-7650782a2530)  

### Test GIF

![Picture Name Here](https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/01095b54-c438-45b1-a361-aad483911552)  



&nbsp;
## Launch_Pad_Part_1
### Assignment Description

The purpose of this assignment is to create a countdown from ten for a rocket launch. You need to use a Raspeberry Pi pico and VS Code.

### Evidence 
<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/449f416f-f686-4f36-bb11-58b909ea0816" 
     width="500" 
     height="500" />
<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/df4820ab-2d22-4d23-8442-0d9be207b481" 
     width="500" 
     height="500" />

### Code
<details open>
<summary>Launch_Pad_Part:1 Code</summary>
<br>
     
```py
import board
import time
import digitalio

while True:
    for x in range(10, -1 ,-1):
        time.sleep(1)
        print(x)
        if x == 0:
            print('LAUNCH')
```

</details>

### Reflection

Originally my code counted up from zero, but to create a negative intervol with the for function you need to start from a large number, go to a small number, but the second number will not be included in the count down. Then you need to create a negative intervol for the for loop. Additionally, the code needs to be uploaded to the Pico through code.py. To access it you need to go to File/Open File/CIRCUITPY (D:)/Code.py.

## Launch_Pad_Part_2_(Lights)

### Assignment Description

In this assignment you have to Countdown from 10 seconds to 0 (liftoff), and print that countdown to the serial monitor.
Additionally, you must blink a red light each second of the countdown, and turn on a green LED to signify liftoff.


### Evidence 
<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/f8316ddd-25bb-409a-8b72-a0fd0cc50da0" 
     width="500" 
     height="500" />

### Wiring
<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/bf7b505e-f29e-4c8c-af55-8ee4954ce572" 
     width="500" 
     height="500" />
     
### Code
<details open>
<summary>Launch Pad Part 2 (Lights) Code</summary>
<br>
     
```py
import board
import time
import digitalio

ledRed = digitalio.DigitalInOut(board.GP0)
ledRed.direction = digitalio.Direction.OUTPUT
ledGreen = digitalio.DigitalInOut(board.GP1)
ledGreen.direction = digitalio.Direction.OUTPUT
count = 0

while True:
    for x in range(10, -1 ,-1): # for loop, in range(FROM THIS NUM, TO THIS NUM, AT THIS INTERVOL)
        if count == 0:
            if x > 0:
                print(x)
            if x == 0:
                print('LAUNCH')
                ledGreen.value = True # LED ON
                count = 1
            ledRed.value = True  #TIMED BLINK--
            time.sleep(0.5)      #--
            ledRed.value = False #--
            time.sleep(0.5)      #--
        else:
            print('Countdown Finished')
```

</details>


### Reflection

Problems I had were the light setup code, the direction of the lights, and  preventing the code from printing 0:
* The light setup code requires a lot of folder retrieval from libraries. It confused me, but I looked it up and now its right.
* The direction of the lights is OUTPUT, make sure to specify otherwise whenever they turn on they won't and you'll get a positive value.
* The code prints 0 at the end of the count down, if I removed zero from the count down, it would be 9 seconds instead of 10, my solution was to print the number when x was greater than 0, simple solve, hours of pain.
  
## Launch_Pad_Part_3_(Button)

### Assignment Description

This assignment uses the last assignment and you need to add a button so the countdown starts when the button is clicked, and then also add an abort option.

### Evidence 

<img src="" 
     width="500" 
     height="500" />

### Wiring

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/9a56b67f-c7b0-44ce-98ef-b063dbb52e0c" 
     width="500" 
     height="500" />

### Code
<details open>
<summary>Launch Pad Part 3 (Button) Code</summary>
<br>
     
```py
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
```

</details> 

### Reflection

Three things that went wrong were the countdown debounce optimization, the abort button, and the buttons input pullup: 

* If the debounce is too long, the code is really blocky and barely works, if its too short it auto aborts.
* The abort function took a while too find, still isn't 100% reliable, something about how the function stops the code doesn't always work on VS Code.
* The input pullup up took too long because the pins on the pico connect in weird ways so the "highways" can have multiple pins sprouting from them, but they can't receive more than one input.

## Launch_Pad_Part_4_(Servo)

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/3e8f446a-a3c5-43f9-a47a-0bc65d0482e1" 
     width="500" 
     height="500" />
     
### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code

<details open>
<summary>Launch_Pad_Part_4_(Servo) Code</summary>
<br>
     
```py

import board                                   
import time
import digitalio
import pwmio
from adafruit_motor import servo

pwm_servo = pwmio.PWMOut(board.GP22, duty_cycle=2 ** 15, frequency=50)
redLED = digitalio.DigitalInOut(board.GP0) 
greenLED = digitalio.DigitalInOut(board.GP1)
button = digitalio.DigitalInOut(board.GP15)
redLED.direction = digitalio.Direction.OUTPUT
greenLED.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

servo1.angle = 0
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
```
</details> 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

## Crash_Avoidance_Part_1_(Accelerometer)

### Assignment Description

In this assignment you have to wire an accelerometer and print its values as its collecting them.
### Evidence 

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/728d734d-636a-49ac-937d-48bd788d310d" 
     width="500" 
     height="500" />
     
### Wiring

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/f8bc2aac-c169-47cb-9b3a-596fbcb2f2a4" 
     width="500" 
     height="500" />
     
### Code

<details open>
<summary>Crash Avoidance Part 1 (Accelerometer) Code</summary>
<br>
     
```py

import adafruit_mpu6050
import busio
import board                                   
import time
import digitalio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("My Values:")
    print(mpu.acceleration)
    time.sleep(1)
```
</details> 

### Reflection

There are three things that went wrong:
* Units: They're in m / s^2. If you're printing units make sure to add that.
* Wiring: SDA and SCL are located on the GP14 and GP15 wires respectfully.
* Direction: The board has the directions its facing written on it. 

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

### Test Image

### Test GIF
