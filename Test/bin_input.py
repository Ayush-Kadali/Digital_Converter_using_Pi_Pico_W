from machine import Pin
import utime
import buzzer


no_of_led = 12

led = [Pin(i, Pin.OUT) for i in range(no_of_led)]

button_0 = Pin(14, mode=Pin.IN)
button_1 = Pin(15, mode=Pin.IN)

def bin_input():
    bin_str = "0b"
    for i in range(12):
        led[i].off()
    count = 0
    while count < 12:
        if (button_0.value() == 1 and button_1.value() ==0):
            led[11-count].off()
            count+=1
            bin_str += "0"
            

        if (button_0.value() == 0 and button_1.value() ==1):
            led[11-count].on()
            count+=1
            bin_str += "1"

        print(count)
        utime.sleep(.11)
    buzzer.play_tone(500)
    return bin_str
        

print(bin_input())
