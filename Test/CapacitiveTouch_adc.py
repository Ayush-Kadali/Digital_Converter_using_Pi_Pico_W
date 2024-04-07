from machine import Pin, ADC
import time


# Create an ADC object linked to pin 26
adc = ADC(Pin(26, mode=Pin.IN))

while True:

    # Read ADC and convert to voltage
    val = adc.read_u16()
    val = val * (3.3 / 65535)
    print(round(val, 2), "V") # Keep only 2 digits

    # Wait a bit before taking another reading
    time.sleep_ms(100)
