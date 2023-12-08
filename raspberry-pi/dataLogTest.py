#type:ignore
import adafruit_bus_device
import busio
import board                                   
import time
import adafruit_mpu6050
import adafruit_mpl3115a2

sda_pin = board.GP14
scl_pin = board.GP15

i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
mpl = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)

st = time.monotonic()

mpl.sealevel_pressure = 1021.3

while True:
    with open("/data.csv", "a") as datalog:
        ct = time.monotonic()
        datalog.write(f"{float(ct)},{round(mpu.gyro[0],3)},{round(mpu.gyro[1],3)},{round(mpu.gyro[2],3)},{mpu.acceleration[2]}, {round(mpl.pressure)}, {round(mpl.altitude)}, {round(mpl.temperature)}\n")
        time.sleep(0.5)
        datalog.flush()