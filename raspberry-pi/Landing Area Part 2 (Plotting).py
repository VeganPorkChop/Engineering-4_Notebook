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
