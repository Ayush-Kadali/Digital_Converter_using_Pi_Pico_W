from machine import I2C, Pin
import utime
from pico_i2c_lcd import I2cLcd
import buzzer


no_of_led = 12

led = [Pin(i, Pin.OUT) for i in range(no_of_led)]

button_0 = Pin(14, mode=Pin.IN)
button_1 = Pin(15, mode=Pin.IN)

def button_interrupt_INT(pin):         # PB_Switch Interrupt handler
    global stop_conversion  # Flag to stop convert()
    global count
    count = 0
    global bin_str
    bin_str = "0b"
    for i in range(12):
        led[i].off()
    if button_interrupt.value() == 1:  # Button press detected
        if stop_conversion:  # If stopping conversion
            print("Interrupt: Resuming Conversion")
            stop_conversion = False  # Reset stop flag
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr("Bin:")

        else:  # If conversion not running (or just finished)
            print("Interrupt: Stopping Conversion")
            stop_conversion = True  # Set stop flag
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr("Bin:")
        
    
    button_interrupt.irq(handler=button_interrupt_INT)
    

def bin_input():
    global bin_str
    bin_str = "0b"
    for i in range(12):
        led[i].off()
    global count
    count = 0
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Bin:")
    while count < 12 :
        if (button_0.value() == 1 and button_1.value() ==0):
            led[11-count].off()
            count+=1
            bin_str += "0"
            lcd.putstr("0")

            

        if (button_0.value() == 0 and button_1.value() ==1):
            led[11-count].on()
            count+=1
            bin_str += "1"
            lcd.putstr("1")

        utime.sleep(.12)
    buzzer.play_tone(500)
    print(bin_str)
    return bin_str
        


def bin_to_dec(bin_num):
    return int(bin_num, 2)

def bin_to_hex(bin_num):
    return hex(int(bin_num, 2))[2:]

def bin_to_oct(bin_num):
    return oct(int(bin_num, 2))[2:]

def bin_to_excess3(bin_num):
    decimal = bin_to_dec(bin_num)
    return bin(decimal+3)[2:]

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
    elif data_type == "EX3":
        result = bin_to_excess3(bin_num)
    elif data_type == "GRY":
        result = bin_to_gray(bin_num)
    
    lcd.move_to(0, 0)
    lcd.putstr("Bin:{}\n".format(bin_num))
    lcd.move_to(0, 1)  # Move to the second row
    # Only update the characters that change
    lcd.putstr("{:<16}".format("{}:{}".format(data_type, result)))

def input_available():
    return button_pin.value() == 0  # Assuming the button pin is grounded when pressed

def convert():
    data_types = ["Dec", "Hex", "Oct", "EX3", "GRY"]
    current_data_type_index = 0
    global run  # Access the global run variable
    global stop_conversion  # Flag to stop convert()

    while True:
        stop_conversion = False  # Reset stop flag before starting conversion
        bin_num = bin_input()[2:]
        convert_and_display(data_types[current_data_type_index], bin_num)

        while run and not stop_conversion:  # Loop until interrupted or stop flag set
            utime.sleep(1)
            current_data_type_index = (current_data_type_index + 1) % len(data_types)
            convert_and_display(data_types[current_data_type_index], bin_num)



        
if __name__ == "__main__":

    global lcd
    i2c = I2C(0, sda=Pin(20), scl=Pin(21))
    I2C_ADDR = i2c.scan()[0]
    lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
    
    global button_interrupt
    button_interrupt = machine.Pin(22,machine.Pin.IN,machine.Pin.PULL_DOWN)
    button_interrupt.irq(trigger=Pin.IRQ_RISING, handler=button_interrupt_INT)
    
    global button_interrupt_State
    button_interrupt_State = button_interrupt.value()
    print("button_interrupt State=", button_interrupt_State)
    global run
    run = True
    global stop_conversion
    stop_conversion = False 
    global state
    state = 0
    for i in range(12):
        led[i].off()
    convert()
    


