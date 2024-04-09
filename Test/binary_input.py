from machine import Pin
import utime

button_0 = Pin(14, mode=Pin.IN)
button_1 = Pin(15, mode=Pin.IN)
while True:
    if (button_0.value() == 1 and button_1.value() ==0):
        print("0")
    if (button_0.value() == 0 and button_1.value() ==1):
        print("1")
    utime.sleep(.5)