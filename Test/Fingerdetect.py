
from machine import Pin

pin_sensor = Pin(26, mode=Pin.IN, pull=Pin.PULL_UP)

while True:
    if pin_sensor.value() == 1:
        print("Finger detected")

