import adafruit_mpu6050
import busio
import board                                   
import time
import digitalio

led = digitalio.DigitalInOut(board.GP20)
led.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

st = time.monotonic()
tilt = False

while True:
    with open("/data.csv", "a") as datalog:
        ct = time.monotonic()
        if mpu.acceleration[2] < 9:
            led.value = True
            tilt = True
        else:
            led.value = False
            tilt = False
        datalog.write(f"{float(ct)},{round(mpu.gyro[0],3)},{round(mpu.gyro[1],3)},{round(mpu.gyro[2],3)},{str(tilt)},{mpu.acceleration[2]}\n")
        time.sleep(0.5)
        datalog.flush()