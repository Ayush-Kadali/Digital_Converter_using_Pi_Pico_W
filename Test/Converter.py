
from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep

@asm_pio(out_init=(rp2.PIO.OUT_HIGH,) * 12, out_shiftdir=PIO.SHIFT_RIGHT, autopull=True, pull_thresh=16)
def convert():
    pull()  
    out(pins, 12)  

convert = StateMachine(0, convert, freq=10000000, out_base=Pin(0))
convert.active(1)

for i in range(4096):
    convert.put(i)
    sleep(.2)
        

convert.put(0)
