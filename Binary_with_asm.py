
from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep

@asm_pio(out_init=(rp2.PIO.OUT_HIGH,) * 12, out_shiftdir=PIO.SHIFT_RIGHT, autopull=True, pull_thresh=16)
def display():
    pull()  
    out(pins, 12)
    
    
def bin_to_gray(bin_num):
    bin_str = str(bin_num)  # Convert integer to string
    result = ''
    result += bin_str[0]
    for i in range(1, len(bin_str)):
        result += str(int(bin_str[i - 1]) ^ int(bin_str[i]))
    return result
def decimal_to_binary(n):
    n = int(n)
    return bin(n).replace("0b", "")

display = StateMachine(0, display, freq=10000000, out_base=Pin(0))
display.active(1)

def binary():
    for i in range(4096):
        display.put(i)
        sleep(.2)
    display.put(0)

        
def gray():
    for i in range(4096):
        num = bin_to_gray(decimal_to_binary(i))
        print(num)
        display.put(num)
        sleep(.2)
    display.put(0)


display.put(0)



