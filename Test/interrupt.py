import machine
import utime


Warning_LED = machine.Pin(0,machine.Pin.OUT)  #Create an output pin for warning LED
Warning_LED.value(0)                           #Set it to OFF


def Pb_Switch_INT(pin):         # PB_Switch Interrupt handler
    global Pb_Switch_State      # reference the global variable
    Pb_Switch.irq(handler=None) # Turn off the handler while it is executing
    
    
    if (Pb_Switch.value() == 1) and (Pb_Switch_State == 0):  # Pb_Switch is active (High) and Pb_Switch State is currently Low
    #if (Pb_Switch.value() == 1): # Pb_Switch is active (High)
        Pb_Switch_State = 1     # Update current state of switch
        Warning_LED.value(1)    # Do required action here
        print("ON")             # Do required action here 
        
            
    elif (Pb_Switch.value() == 0) and (Pb_Switch_State == 1): # Pb_Switch is not-active (Low) and Pb_Switch State is currently High
    #elif (Pb_Switch.value() == 0): # Pb_Switch is not-active (Low)
        Pb_Switch_State = 0     # Update current state of switch
        Warning_LED.value(0)    # Do required action here
        print("OFF \n")         # Do required action here

    Pb_Switch.irq(handler=Pb_Switch_INT)
    

#Creat an 'object' for our Pb_Switch change of state
Pb_Switch = machine.Pin(22,machine.Pin.IN,machine.Pin.PULL_DOWN)
#Setup the Interrupt Request Handling for Pb_Switch change of state
Pb_Switch.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=Pb_Switch_INT)


#Preset the STATE variable for the Pb_Switch
Pb_Switch_State = Pb_Switch.value()
print("Pb_Switch State=", Pb_Switch_State)

# A loop just to keep things running, but does nothing constructive
print("Ready, Set, Go!")
while True:  #run an endless loop as the main loop
    utime.sleep(.0001)
    #Perform all other activites here














#######################################################################################
#Setup the Interrupt Request Handling for Pb_Switch change of state
Pb_Switch.irq(trigger=machine.Pin.IRQ_RISING, handler=Pb_Switch_INT)
Pb_Switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=Pb_Switch_INT)
Pb_Switch.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=Pb_Switch_INT)


