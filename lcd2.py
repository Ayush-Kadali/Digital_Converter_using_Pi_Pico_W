import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


I2C_ADDR     = 38
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(1, sda=Pin(26), scl=Pin(27), freq=400000)
lcd2 = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

    


def MIT_LOGO():
    
    #Panel 00      
    lcd2.custom_char(0, bytearray([
    0x00,
    0x00,
    0x00,
    0x00,
    0x01,
    0x02,
    0x05,
    0x05
        
        ]))
    
    #Panel 10      
    lcd2.custom_char(1, bytearray([
    0x1F,
    0x1F,
    0x15,
    0x1F,
    0x00,
    0x1F,
    0x15,
    0x15
        ]))
    
    
    
    
    #Panel 01
    lcd2.custom_char(2, bytearray([
    0x00,
    0x04,
    0x04,
    0x1F,
    0x1B,
    0x0A,
    0x11,
    0x11

        
        ]))
    
    #Panel 11
    lcd2.custom_char(3, bytearray([
    0x1F,
    0x1F,
    0x15,
    0x1F,
    0x00,
    0x0E,
    0x04,
    0x0E


        
        ]))
    
    #Panel 02
    lcd2.custom_char(4, bytearray([
    0x00,
    0x00,
    0x00,
    0x00,
    0x10,
    0x08,
    0x14,
    0x14
        
        ]))

    #Panel 12
    lcd2.custom_char(5, bytearray([
    0x1F,
    0x1F,
    0x15,
    0x1F,
    0x00,
    0x0E,
    0x04,
    0x04

        
        ]))
  
    lcd2.move_to(0,0)
    lcd2.putchar(chr(0))
    lcd2.move_to(0,1)
    lcd2.putchar(chr(1))
    lcd2.move_to(1,0)
    lcd2.putchar(chr(2))
    lcd2.move_to(1,1)
    lcd2.putchar(chr(3))
    lcd2.move_to(2,0)
    lcd2.putchar(chr(4))
    lcd2.move_to(2,1)
    lcd2.putchar(chr(5))
    
    
  

def textscroll(length,string):
    x = lcd2.cursor_x
    y = lcd2.cursor_y
    i=0
    for i in range(len(string)-length+1):
        updated_str = string[i:i+length]
        lcd2.move_to(x,y)
        lcd2.putstr(" "*length)
        lcd2.move_to(x,y)
        lcd2.putstr(updated_str)
        i += 1
        utime.sleep(1)

    

    
def lcd_2():
    MIT_LOGO()

    while True:
        lcd2.move_to (6,0)
        lcd2.putstr("MIT-WPU")
        lcd2.move_to(4,1)
        lcd2.putstr(" Group : 07")
        utime.sleep(5)
        lcd2.move_to(4,1)
        string = "FCASD MiniProject"
        textscroll(11,string)
        utime.sleep(10)


lcd_2()

