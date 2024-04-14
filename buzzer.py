from picozero import Speaker
from time import sleep
import math

# Define frequencies for high and low tones
HIGH_FREQ = 1000  # Adjust for desired high frequency (Hz)
LOW_FREQ = 100   # Adjust for desired low frequency (Hz)

# Define duration of each tone
DURATION = 0.4  # Adjust for desired tone duration (seconds)
DELAY = 0.1 # Duration between each char

speaker = Speaker(13)


def play_tone(frequency):
    speaker.play(int(frequency), duration=DURATION)  # Play tone with specified frequency and duration
    sleep(DELAY)

def play_binary(binary_string):
    # Define frequencies for high and low tones
    FREQ_1 = 1000  
    FREQ_0 = 500  

    for bit in binary_string:
        if bit == "1":
            play_tone(FREQ_1)
        else:
            play_tone(FREQ_0)



def calculate_frequency(base, index, min_freq=200, max_freq=5000):
    """Calculates frequency based on position within a number system."""
    return round(min_freq + (index / (base - 1)) * (max_freq - min_freq), 2)

def play_octal(octal_string):
    base = 8
    frequencies = [calculate_frequency(base, i) for i in range(base)]

    for digit in octal_string:
        index = int(digit)
        play_tone(frequencies[index])

def play_decimal(decimal_string):
    base = 10
    frequencies = [calculate_frequency(base, i) for i in range(base)]

    for digit in decimal_string:
        index = int(digit)
        play_tone(frequencies[index])

def play_hexadecimal(hexadecimal_string):
    base = 16
    frequencies = [calculate_frequency(base, i) for i in range(base)]

    for digit in hexadecimal_string:
        index = int(digit, 16)  # Handle both digits and letters (A-F)
        #index = value if value < 10 else value - 10  # Adjust index for A-F
        play_tone(frequencies[index])

# play_binary("010101")
# play_octal("01234567")
# sleep(1)
# 
# play_decimal("0123456789")
# sleep(1)
# 
# play_hexadecimal("0123456789ABCDEF")
# 
# 
# while True:
#     binary_input = input("Enter a binary number: ")
#     play_binary(binary_input)
# '''
# for i in range(15000,20000):
#     speaker.play(i,0.000001)
#     print(i)
# '''
# 