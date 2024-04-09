from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
while True:
  bin_num = str(input("Enterr the number in binary : "))
  lcd.clear()
  f_bin = int(bin_num,2)
  hex_num =hex(f_bin)
  lcd.move_to(0,0)
  lcd.putstr("Bin: "+(bin_num)+"\n")
  lcd.move_to(0,1)
  lcd.putstr("Hex: "+(hex_num[2:]))
