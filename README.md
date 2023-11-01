
# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Launch Pad (part 1)](#launch_pad_part_1)
* [Raspberry_Pi_Launch Pad (part 2)](#launch_pad_part_2_lights)
* [Raspberry_Pi_Launch Pad (part 3)](#launch_pad_part_3_button)
* [Raspberry_Pi_Launch Pad (part 4)](#launch_pad_part_4_servo)
* [Crash Avoidance Part 1 (Accelerometer)](#crash_avoidance_part_1_accelerometer)
* [Crash Avoidance Part 2 (Light + Power)](#crash_avoidance_part_2_light__power)
* [Crash Avoidance Part 3 (OLED Screen)](#crash_avoidance_part_3_oled_screen)
* [Crash Avoidance Part 4 (Altimeter)](#crash_avoidance_part_4_altimeter)
* [Landing Area Part 1 (Functions)](#landing_area_part_1_functions)

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

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/3ffdb983-a4a6-4f69-bb49-0933b13652a5" 
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
                    print(x) # Prints for loop val
                if x == 0:
                    print('LAUNCH')
                    ledGreen.value = True
                    time.sleep(0.1)
                    print('Countdown Finished!')
                    time.sleep(5)
                ledRed.value = True   #Blinks Light--
                time.sleep(0.5)       --
                ledRed.value = False  --
                time.sleep(0.5)       --
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

Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor.
Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.
Include a physical button that starts the countdown. 
Actuate a 180 degree servo on liftoff to simulate the launch tower disconnecting.


### Evidence 

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/3e8f446a-a3c5-43f9-a47a-0bc65d0482e1" 
     width="500" 
     height="500" />
     
### Wiring

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/ffa1c174-23d2-43bb-8854-a5f325e925d5" 
     width="500" 
     height="500" />


### Code

<details open>
<summary>Launch_Pad_Part_4_(Servo) Code</summary>
<br>
     
```py

import board                 # Imports                  
import time                  -
import digitalio             -
import pwmio                 -
from adafruit_motor import servo

pwm_servo = pwmio.PWMOut(board.GP22, duty_cycle=2 ** 15, frequency=50) # sets frequency of pin, idk how it works, visit(https://docs.circuitpython.org/en/latest/shared-bindings/pwmio/index.html)
redLED = digitalio.DigitalInOut(board.GP0) 
greenLED = digitalio.DigitalInOut(board.GP1)
button = digitalio.DigitalInOut(board.GP15)
redLED.direction = digitalio.Direction.OUTPUT
greenLED.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500) # this sets the allowed pulses and also creates an object in code

servo1.angle = 0 #setting initial values
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
    while count > 0 & count <= 3: # begins turning servo
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

Three things went wrong with this assignment:
* The servo spinning is very blocky if you chunk the code and move the servo _x_ degrees every loop. So instead I spent 2 classes making it smooth by creating delays and timed intervol and moved it three degrees at a time.
* The abort button was difficult to employ, so, sense it isn't required, I deleted it.
* when you ask an object what its value is, you have to type: _object_.value

## Crash_Avoidance_Part_1_(Accelerometer)

### Assignment Description

In this assignment you have to wire an accelerometer and print it's values as it's collecting them.

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

import adafruit_mpu6050    # Imports
import busio               -
import board               -                             
import time                -
import digitalio           -

sda_pin = board.GP14                # Defining SDA and SCL pins
scl_pin = board.GP15                -
i2c = busio.I2C(scl_pin, sda_pin)   # defining i2c function
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("My Values:")      # Printing values
    print(mpu.acceleration)  -
    time.sleep(1)
```
</details> 

### Reflection

There are three things that went wrong:
* Units: They're in m / s^2. If you're printing units make sure to add that.
* Wiring: SDA and SCL are located on the GP14 and GP15 wires respectfully.
* Direction: The board has the directions its facing written on it.

## Crash_Avoidance_Part_2_(Light_+_Power)

### Assignment Description

The module must have an accelerometer that continuously reports x, y, and z acceleration values. The module must have an LED that turns on if the helicopter is tilted to 90 degrees. The module must be powered by a mobile power source.

### Evidence 

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/7b947c59-2882-44f2-b5fd-6fffe093cfe6" 
     width="500" 
     height="500" />

### Wiring

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/d96d4a5e-8852-4ea4-80bd-810e1df7fdd8" 
     width="500" 
     height="500" /> 

### Code

<details open>
<summary>Crash Avoidance Part 2 (Light + Power) Code</summary>
<br>
     
```py
import adafruit_mpu6050
import busio
import board                                   
import time
import digitalio

led = digitalio.DigitalInOut(board.GP0)         # pin setup
led.direction = digitalio.Direction.OUTPUT      --

sda_pin = board.GP14                            --
scl_pin = board.GP15                            --
i2c = busio.I2C(scl_pin, sda_pin)               --
mpu = adafruit_mpu6050.MPU6050(i2c) # i2c, idk how it works, look here, https://adafruit.github.io/Adafruit_MPU6050/html/class_adafruit___m_p_u6050.html

while True:
    led.value = False
    print(mpu.acceleration)
    while mpu.acceleration[2] < 0.95: # mpu.acceleration[2], value of only the z axis 
        led.value = True
        print(mpu.acceleration) # prints all acceleration values

```
</details>

### Reflection

Two things went wrong with this assignment:
* I used the wrong function. I was using mpu.gyro, which measures acceleration of rotation. The correct way to do this was to measure the acceleration based on gravity.
* I put the less than symbol the wrong way. The acceleration of gravity on the y axis is greater than .95 UNTIL it reaches about a 90* tilt.

## Crash_Avoidance_Part_3_(OLED_Screen)

### Assignment Description

In this assignment the The module must have an accelerometer that continuously reports x, y, and z acceleration values. The module must have an LED that turns on if the helicopter is tilted to 90 degrees. The module must be powered by a mobile power source. The module must have an onboard screen that prints x, y, and z angular velocity values (rad/s) rounded to 3 decimal places.


### Evidence 

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/9a49bd0d-6387-49b2-b66c-60c224dc0ea0" 
     width="500" 
     height="500" /> 

### Wiring

<img src="https://mail.google.com/mail/u/0?ui=2&ik=33ad3a32c0&attid=0.1&permmsgid=msg-f:1777749083368132753&th=18abd55f55ef1091&view=att&disp=safe" 
     width="500" 
     height="500" /> 
     
### Code

<details open>
<summary>Crash_Avoidance_Part_3_(OLED_Screen) Code</summary>
<br>
     
```py
import adafruit_mpu6050                    #Imports:--
import busio                               #--
import board                               #--  
import time                                #--
import digitalio                           #--
from adafruit_display_text import label    #--
import adafruit_displayio_ssd1306          #--
import terminalio                          #--    
import displayio                           #--

displayio.release_displays() #initializes displays

sda_pin = board.GP14 #init SDA pin
scl_pin = board.GP15 #init SCL pin


i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

# create the display group
splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)

while True:
    # the order of this command is (font, text, text color, and location)
    text_area.text = f"Rotation: \n X:{round(mpu.gyro[0],3)} \n Y:{round(mpu.gyro[1],3)} \n Z:{round(mpu.gyro[2],3)}"
    led.value = False
    print(mpu.acceleration)
    while mpu.acceleration[2] < 0.95: 
        led.value = True
        print(mpu.acceleration)
        text_area.text = f"Rotation: \n X:{round(mpu.gyro[0],3)} \n Y:{round(mpu.gyro[1],3)} \n Z:{round(mpu.gyro[2],3)}"
```
</details>

### Reflection

Three Things went Wrong:
* the fString. If you want to format an fString go to this site: https://github.com/adafruit/circuitpython/issues/4723
* The I2C adresses. Adding another adress to the I2C mixed everything up. I didn't have enought space on the bread board so I had to move some pins around, in turn, this messed up my wiring and I had to redo it.
* Finding the I2C adress. The code for this is located here. It took a while to get the wiring right.

## Crash_Avoidance_Part_4_(Altimeter)

### Assignment Description

The module must have an accelerometer that continuously reports x, y, and z acceleration values.
The module must have an LED that turns on if the helicopter is tilted to 90 degrees. 
The module must be powered by a mobile power source. 
The module must have an onboard screen that prints x, y, and z angular velocity values (rad/s).
The module should NOT show a warning light if the device is more than 3 meters above its starting point.

### Evidence 

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/2f70fd7a-791e-49c4-b6dd-c8438e9d9722" 
     width="500" 
     height="500" />
     
### Wiring

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/768f124e-2b9d-4ccc-bb66-46fa339f5b07" 
     width="500" 
     height="500" /> 
     
### Code

<details open>
<summary>Crash Avoidance Part 4 (Altimeter) Code</summary>
<br>
     
```py


import adafruit_mpu6050
import busio
import board                                   
import time
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import adafruit_mpl3115a2

displayio.release_displays()

sda_pin = board.GP14
scl_pin = board.GP15

i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)

# create the display group
splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)

tim = sensor.altitude

while True:
     # the order of this command is (font, text, text color, and location)
    text_area.text = f"Rotation: Altitude: \n X:{round(mpu.gyro[0],3)} {round(sensor.altitude, 3)}m \n Y:{round(mpu.gyro[1],3)} Pressure: \n Z:{round(mpu.gyro[2],3)} {round(sensor.pressure, 3)}Pa"
    print(mpu.acceleration)
    if mpu.acceleration[2] < 0.95 and sensor.altitude < tim + 3: 
        led.value = True
    else:
        led.value = False
    
```
</details>

### Reflection

Two Things Went Wrong:
* The wiring: I Stripped everything before taking a video.
* I couldn't get the I2C function to work, the problem was the wiring, make sure that the GND rail on your breadboard is connected to GND on your pico.

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

## FEA_Part_1_(Beam_Design)

### Assignment Description

A beam must stick straight out from a predetermined platform, and the beam gets a bucket screwed into the side of it, then weight gets added. You need to maximize the ammount of weight that that bucket can hold. This is constrained by these contraints:
* The beam must use the provided attachment block with no modifications
* The beam with the attachment block must be able to fully engage with the holder
* The beam must use the example eye bolt mounting geometry
* The center of the eyebolt hole must be 180 mm from the front face of the attachment block (in a direction perpendicular to the front face)
* No part of the beam may extend below the bottom face of the attachment block
* All vertical angles must be >= 45° measured relative to the horizontal plane (no overhangs)
* The beam must be PLA material
* The entire beam, including attachment block, must weight <= 13 grams

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/92a40a9416b5315e6a429686/w/2b2c3d00de9869597b85e9c4/e/d26c7202e8ba614aecbc70b2)

### Part Image

![](https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/208aaf0e-65b5-4077-bf3f-16a580161035)

### Reflection

For this assignment, three things went wrong:
* The weight of the object was way too large, so we took advantage of the fact that the nozel is 0.04mm. We removed a 0.03mm layer so that the computer would think that it weighs less than it actually does.
* We had too much weight again, so this time we filleted the edges down.
* Originally, the document was unable to be copyed, so we spent a portion of the first class trying to export the object and import it into our own doc which eventually failed because STEP files dont save individual parts, so we couldnt accuratly measure weight.

## FEA_Part_3_(Analysis)

### Assignment Description

For this assignment we were instructed to take our previous part and use FDA to analyse the stress on our part. We Examined the beams we just created in Onshape, and try to optimize the beam in two ways. Our goal was to minimize beam bending while maximizing the mass the beam can support before failing.

### Part Link 

[Onshape Link](https://cvilleschools.onshape.com/documents/92a40a9416b5315e6a429686/w/2b2c3d00de9869597b85e9c4/e/d26c7202e8ba614aecbc70b2)

### Part Image

![](https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/835d7772-9255-4fef-b6d9-5831a0995b86)

### Reflection

The FDA simulation forced us to make a big decision fix our curent design or scrap it and start over with the new information we have learned. We decided to do both and redesign the previous part in a new part studio with some new additions. This proved to be the most efective path as we where much faster in creating the new part. Unfortunatly, this was a group project and one of the two groupmates, Jakob, didn't manage to help.

## FEA_Part_4_(Iterative_Design)

### Assignment Description

After simulation, you should have an idea of where your beam needs to improve. Now you’ll enter the iterative design cycle. Improve the beam based on your findings from the FEA simulation, then simulate again. You should be able to dramatically reduce the maximum stress and bending of the beam over the course of several simulations and redesigns. 

### Part Link 

[ENGR4 Beam Starter Document - Graham and Jacob](https://cvilleschools.onshape.com/documents/92a40a9416b5315e6a429686/w/2b2c3d00de9869597b85e9c4/e/0af744a4e82b10b8a53d9b22)

### Part Image

![Assembly 1](https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/97dc9db0-4a3e-4a36-9487-72c039fae1a8)

### Reflection

Three things went wrong:
* When creating the force, the window that pops up prompt you for a direction based on a mate connecter, an instance and the option to load a region. LOAD THE REGION, without any regions loaded, my design holds 25 lbs of force, but with the loading it holds 5.

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/49f29cfd-e078-4d79-890d-97ece9d93a4b" 
     width="500" 
     height="500" />
     
* Holes in designs are very useful, sense the restrictions were revolved around us not being allowed to create overhangs over 45*, I was at a loss as to how to make the design better, but, we're allowed to use holes at the maximum size of 5mm. These holes take away unnessisary material and allow you to use it elsewhere.
* Corners of builds are considered breakpoints, this is because all of the stress is compiled into one small edge. Use the fillet tool to reduce this problem, but not the chamfer because that tool doesnt allow for curveness, and that's a nesesity for structural integrity.

Improvments:
* N/A, our sedign in more complicated and gholds the same weight due to an unfortunate mishap.
* Designing speed, I spent 8 hours designing this incorrectly, I learned how to OnShape faster and thats it.

## Landing_Area_Part_1_(Functions)

### Assignment Description

In this assignment you had to make a computer calculate the area of a triangle based off of three inputed coordanites.

### Evidence 

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/a50c329c-2a9d-4564-b2cf-bb0d3bf640ee" 
     width="500" 
     height="500" />

### Code

<details open>
<summary>Landing Area Part 1 (Functions) Code</summary>
<br>
     
```py
import time # imports
x1 = 0 # variable values
x2 = 0 -
x3 = 0 -
y1 = 0 -
y2 = 0 -
y3 = 0 -

def triangle(x1, y1, x2, y2, x3, y3):# defininf function
    try:
        pointArray = Input.split(",")
        x1 = float(pointArray[0]) # Points location in the array
        y1 = float(pointArray[1]) -
        x2 = float(pointArray[2]) -
        y2 = float(pointArray[3]) -
        x3 = float(pointArray[4]) -
        y3 = float(pointArray[5]) -
        p = (abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2.0  # finding the area of the triangle
        return p
    except:
        print("Uh Oh. Do it again.") #error message
        p = 0
        return p

while True:
    Input = input("Points: ")# taking input from computer prompt

    area = triangle(x1, y1, x2, y2, x3, y3)# calling defined function
    if area == 0:  # error for triangle not working
        print("Are you sure thats a triangle?")
        continue
    else:
        print("Here is yo area! " + str(area)) # writing the triangle area
```
</details>

### Reflection

Three things went wrong:
* To find the area of a triangle you have to find the absolute value of the number, line 17, you can't use "||" signs, instead you have to use the function abs().
* When taking inputs, you can spling the string into arrays using the object.split() function. This turns your points into ARRAYS, you still have to call the value based off of its location in the array.
* To print the points you have to turn them into strings otherwise the computer gets mad at you.


## Landing Area Part 2 (Plotting)

### Assignment Description

The code must ask for the user to input a set of three coordinates in (x,y) format
The triangle area must be determined using a function
If the user inputs coordinates incorrectly (letters or improper format) the code should return to the input stage, it should not throw an error or exit the script
The triangle area must be printed to the screen in this format: “The area of the triangle with vertices (x,y), (x,y), (x,y) is {area} square km.
The code must return to the input stage after printing the area, and wait for user input.
An onboard OLED screen must plot each triangle on a graph relative to the base location.

### Evidence 

<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/5a7157d1-0113-4fa9-b29e-38e290ed0671" 
     width="500" 
     height="500" />

### Wiring

![](https://content.instructables.com/FLK/I4IF/L92SC6MX/FLKI4IFL92SC6MX.jpg?auto=webp&frame=1&fit=bounds&md=9e160d0ed8c68131c471190b64f3174e)

### Code

<details open>
<summary>Landing Area Part 1 (Functions) Code</summary>
<br>
     
```py
import adafruit_display_shapes
import busio
import board
import time
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import adafruit_mpl3115a2
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

displayio.release_displays()

sda_pin = board.GP14
scl_pin = board.GP15

splash = displayio.Group()

i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0

title = "Graph"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)

def triangle(x1, y1, x2, y2, x3, y3):
    try:
        sametriangle = False
        
        if Input == Input:
            sametriangle = True
        pointArray = Input.split(",")
        x1 = float(pointArray[0])
        y1 = float(pointArray[1])
        x2 = float(pointArray[2])
        y2 = float(pointArray[3])
        x3 = float(pointArray[4])
        y3 = float(pointArray[5])

        triangle = Triangle(int(x1) + 64, 32 - int(y1), int(x2) + 64, 32 - int(y2), int(x3) + 64, 32 - int(y3), outline=0xFFFFFF)
        splash.append(triangle)
        if sametriangle == True:
            
            p = (abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2.0
            return p
        
    except:
        print("Uh Oh. Do it again.")
        p = 0
        return p

    



while True:
    vline = Line(64, 0, 64, 64, color=0xFFFFFF)
    hline = Line(0, 32, 128, 32, color=0xFFFFFF)
    circle = Circle(64, 32, 2, outline=0xFFFFFF)
    splash.append(circle)
    splash.append(hline)
    splash.append(vline)
    Input = input("Points: ")

    area = triangle(x1, y1, x2, y2, x3, y3)
    
    if area == 0:
        print("Are you sure thats a triangle?")
        continue
    else:
        print("Here is yo area! " + str(area))
```
</details>

### Reflection

Two things went wrong with this assignment:
* Plotting the verticies of the triangle has to be done in a certain way. You need to add 64 to the x value and subtract the y value from 32 because of how the boards coordanize system is setup.
* The SDA and SCL pins go to SDA and SCL on the pico, but you also have to use their i2c adress, especially if you made the mistake of using i2c. Its only useful to use adresses if there is more than one thing plugged into the pico through the same pins.

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

### Test Image

### Test GIF
