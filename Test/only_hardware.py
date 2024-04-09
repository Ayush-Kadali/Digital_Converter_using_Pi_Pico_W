from machine import I2C, Pin
import utime
from pico_i2c_lcd import I2cLcd

def bin_to_dec(bin_num):
    return int(bin_num, 2)

def bin_to_hex(bin_num):
    return hex(int(bin_num, 2))[2:]

def bin_to_oct(bin_num):
    return oct(int(bin_num, 2))[2:]

def bin_to_excess3(bin_num):
    decimal = bin_to_dec(bin_num)+3
    return bin(decimal)[2:]

def bin_to_gray(bin_num):
    bin_str = str(bin_num)  # Convert integer to string
    gray_str = ''
    gray_str += bin_str[0]
    for i in range(1, len(bin_str)):
        gray_str += str(int(bin_str[i - 1]) ^ int(bin_str[i]))
    return gray_str

# Add more conversion functions as needed

def convert_and_display(data_type, bin_num):
    
    if data_type == "Dec":
        result = bin_to_dec(bin_num)
    elif data_type == "Hex":
        result = bin_to_hex(bin_num)
    elif data_type == "Oct":
        result = bin_to_oct(bin_num)
    elif data_type == "Xs3":
        result = bin_to_excess3(bin_num)
    elif data_type == "Gray":
        result = bin_to_gray(bin_num)
    
    lcd.move_to(0, 0)
    lcd.putstr("Bin:{}\n".format(bin_num))
    lcd.move_to(0, 1)  # Move to the second row
    # Only update the characters that change
    lcd.putstr("{:<16}".format("{}:{}".format(data_type, result)))

def input_available():
    return button_pin.value() == 0  # Assuming the button pin is grounded when pressed

data_types = ["Dec", "Hex", "Oct", "Xs3", "Gray"]
current_data_type = data_types[0]

i2c = I2C(0, sda=Pin(20), scl=Pin(21))
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

button_pin = Pin(29, Pin.IN, Pin.PULL_UP)  # Assuming pin 10 is connected to the button

while True:
    bin_num = input("Enter the number in binary: ")
    if bin_num == "":  # If Enter is pressed
        break
    
    convert_and_display(current_data_type, bin_num)
    
    while True:

        utime.sleep(1)
        current_data_type = data_types[(data_types.index(current_data_type) + 1) % len(data_types)]
        convert_and_display(current_data_type, bin_num)
