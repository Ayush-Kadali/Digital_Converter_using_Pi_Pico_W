
def setup_web_server():
    print("Core 0: \n Waiting for Wifi...")
    utime.sleep(.2)
    print("Core 1 : Setting up Hardware")
    utime.sleep(2)
    print("Core 0: \n Waiting for Wifi...", end="")

    for i in range(3):
        utime.sleep(1.5)
        print(".",end="")
    print("\n Core 0 : Setting up Wifi")
    print('''Core 0 :
Deploying the website on https://ayush-kadali.github.io/Digital_Converter_using_Pi_Pico_W/ 
''')
    print("Web server Setup Successful")

