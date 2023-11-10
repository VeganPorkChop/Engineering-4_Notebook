import adafruit_mpu6050
import busio
import board                                   
import time
import digitalio

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

st = time.monotonic()
tilt = False

def blink():
    ct = time.monotonic()
    led.value = True
    while time.monotonic < 0.25 + ct:
        time.sleep(0.01)
    led.value = False

with open("/data.csv", "a") as datalog:
    while True:
        ct = time.monotonic()
        led.value = False
        tilt = False
        if mpu.acceleration[2] < 0.95:
            tilt = True
        datalog.write(f"Time Elapsed: {float(ct)} Rotation: X:{round(mpu.gyro[0],3)} Y:{round(mpu.gyro[1],3)} Z:{round(mpu.gyro[2],3)} Tilted:{str(tilt)}\n")
        blink()
        datalog.flush()
        time.sleep(0.25)