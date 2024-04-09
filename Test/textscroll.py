import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

    

lcd.move_to(1,0)
lcd.show_cursor()
string = "FCASD MiniProject"

def textscroll(length,string):
    x = lcd.cursor_x
    y = lcd.cursor_y
    i=0
    while True:
        updated_str = string[i:i+length]
        lcd.move_to(x,y)
        lcd.putstr(" "*length)
        lcd.move_to(x,y)
        lcd.putstr(updated_str)
        i += 1
        utime.sleep(1)
        
textscroll(3, string)
        


