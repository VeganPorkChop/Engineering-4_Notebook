
import adafruit_mpu6050
import busio
import board                                   
import time
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()

sda_pin = board.GP14
scl_pin = board.GP15


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



while True:
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)  
