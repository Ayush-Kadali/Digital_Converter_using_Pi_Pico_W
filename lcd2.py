import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

    


def MIT_LOGO():
    
    #Panel 00      
    lcd.custom_char(0, bytearray([
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
    lcd.custom_char(1, bytearray([
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
    lcd.custom_char(2, bytearray([
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
    lcd.custom_char(3, bytearray([
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
    lcd.custom_char(4, bytearray([
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
    lcd.custom_char(5, bytearray([
    0x1F,
    0x1F,
    0x15,
    0x1F,
    0x00,
    0x0E,
    0x04,
    0x04

        
        ]))
  
    lcd.move_to(0,0)
    lcd.putchar(chr(0))
    lcd.move_to(0,1)
    lcd.putchar(chr(1))
    lcd.move_to(1,0)
    lcd.putchar(chr(2))
    lcd.move_to(1,1)
    lcd.putchar(chr(3))
    lcd.move_to(2,0)
    lcd.putchar(chr(4))
    lcd.move_to(2,1)
    lcd.putchar(chr(5))
    
    
  

def textscroll(length,string):
    x = lcd.cursor_x
    y = lcd.cursor_y
    i=0
    for i in range(len(string)-length+1):
        updated_str = string[i:i+length]
        lcd.move_to(x,y)
        lcd.putstr(" "*length)
        lcd.move_to(x,y)
        lcd.putstr(updated_str)
        i += 1
        utime.sleep(1)

    

    
 
MIT_LOGO()
lcd.move_to (7,0)
lcd.putstr("MIT-WPU")
lcd.move_to(5,1)
lcd.putstr("Group : 07")
utime.sleep(5)
lcd.move_to(4,1)
string = "FCASD MiniProject"
textscroll(11,string)




