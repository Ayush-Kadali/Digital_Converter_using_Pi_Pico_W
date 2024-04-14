from machine import I2C, Pin
import utime
from pico_i2c_lcd import I2cLcd
import buzzer


no_of_led = 12

led = [Pin(i, Pin.OUT) for i in range(no_of_led)]

button_0 = Pin(14, mode=Pin.IN)
button_1 = Pin(15, mode=Pin.IN)

def Pb_Switch_INT(pin):         # PB_Switch Interrupt handler
    global Pb_Switch_State      # reference the global variable
    Pb_Switch.irq(handler=None) # Turn off the handler while it is executing
    global run
    
    if (Pb_Switch.value() == 1) and (Pb_Switch_State == 0):  # Pb_Switch is active (High) and Pb_Switch State is currently Low
    #if (Pb_Switch.value() == 1): # Pb_Switch is active (High)
        Pb_Switch_State = 1     # Update current state of switch
            # Do required action here
        run = False
        print("OFF")
        raise Exception()
    
    
    elif (Pb_Switch.value() == 1) and (Pb_Switch_State == 1):  # Pb_Switch is active (High) and Pb_Switch State is currently Low
    #if (Pb_Switch.value() == 1): # Pb_Switch is active (High)
        Pb_Switch_State = 0     # Update current state of switch
            # Do required action here
        run = True
        print("ON")
        
        
    
    Pb_Switch.irq(handler=Pb_Switch_INT)
    

def bin_input():
    bin_str = "0b"
    for i in range(12):
        led[i].off()
    count = 0
    while count < 12 :
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
    elif data_type == "Gray":
        result = bin_to_gray(bin_num)
    
    lcd.move_to(0, 0)
    lcd.putstr("Bin:{}\n".format(bin_num))
    lcd.move_to(0, 1)  # Move to the second row
    # Only update the characters that change
    lcd.putstr("{:<16}".format("{}:{}".format(data_type, result)))

def input_available():
    return button_pin.value() == 0  # Assuming the button pin is grounded when pressed

def init():

    global lcd
    i2c = I2C(0, sda=Pin(20), scl=Pin(21))
    I2C_ADDR = i2c.scan()[0]
    lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
    
    global Pb_Switch
    Pb_Switch = machine.Pin(22,machine.Pin.IN,machine.Pin.PULL_DOWN)
    Pb_Switch.irq(trigger=machine.Pin.IRQ_RISING, handler=Pb_Switch_INT)
    
    global Pb_Switch_State
    Pb_Switch_State = Pb_Switch.value()
    print("Pb_Switch State=", Pb_Switch_State)
    global run
    run = True
    

def convert():
    data_types = ["Dec", "Hex", "Oct", "EX3", "Gray"]
    current_data_type = data_types[0]
    while run:
        try:
        
            bin_num = bin_input()[2:]
    #         if run == False:
    #             bin_num = ""
    #             break
            convert_and_display(current_data_type, bin_num)

            
            while True:
                utime.sleep(1)
                current_data_type = data_types[(data_types.index(current_data_type) + 1) % len(data_types)]
                convert_and_display(current_data_type, bin_num)
        except Exception:
            print("Hello")
            
