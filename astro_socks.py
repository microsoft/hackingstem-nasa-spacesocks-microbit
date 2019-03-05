# ------------__ Hacking STEM astro_socks.py micro:bit __-----------
#  For use with the TODO:[Add lesson title] 
#  lesson plan available from Microsoft Education Workshop at 
#  http://aka.ms/hackingSTEM
#
#  Overview: This project reads voltage on 4 GPIO pins and writes those values
#  to serial, and reads serial and looks for keywords.
# 
#  Pins:
#  Pin 0 = Toe Sensor
#  Pin 1 = First Mid-foot Sensor
#  Pin 2 = Second Mid-foot Sensor
#  Pin 3 = Ankle Sensor

#  This project uses a BBC micro:bit microcontroller, information at:
#  https://microbit.org/
#
#  Comments, contributions, suggestions, bug reports, and feature
#  requests are welcome! For source code and bug reports see:
#  http://github.com/[TODO github path to Hacking STEM]
#
#  Copyright 2018, Adi Azulay
#  Microsoft EDU Workshop - HackingSTEM
#  MIT License terms detailed in LICENSE.txt
# ===---------------------------------------------------------------===

from microbit import *

# Setup & Config
display.off()  # Turns off LEDs to free up additional input pins
uart.init(baudrate=9600)  # Sets serial baud rate
DATA_RATE = 10 # Frequency of code looping
EOL = '\n' # End of Line Character

# These constants are the pins used on the micro:bit for the sensors
TOE_SENSOR = pin0
FIRST_MID_SENSOR = pin1
SECOND_MID_SENSOR = pin2
ANKLE_SENSOR = pin3


def process_sensors():
    # Reads voltage of from each pin attached to a pressure sensor
    global toe_reading, first_mid_reading, second_mid_reading, ankle_reading
    toe_reading = TOE_SENSOR.read_analog()
    first_mid_reading = FIRST_MID_SENSOR.read_analog()
    second_mid_reading = SECOND_MID_SENSOR.read_analog()
    ankle_reading = ANKLE_SENSOR.read_analog()


#=============================================================================#
#---------------The Code Below Here is for Excel Communication----------------#
#=============================================================================#

# Array to hold the serial data
parsedData = [0] * 5


def getData():
    #   This function gets data from serial and builds it into a string
    global parsedData, builtString
    builtString = ""
    while uart.any() is True:
        byteIn = uart.read(1)
        if byteIn == b'\n':
            continue
        byteIn = str(byteIn)
        splitByte = byteIn.split("'")
        builtString += splitByte[1]
    parseData(builtString)
    return (parsedData)


def parseData(s):
    #   This function seperates the string into an array
    global parsedData
    if s != "":
        parsedData = s.split(",")

#=============================================================================#
#------------------------------Main Program Loop------------------------------#
#=============================================================================#
while (True):
    process_sensors()
    serial_in_data = getData()
    if (serial_in_data[0] != "#pause"):
        # uart is the micro:bit command for serial
        uart.write('{},{},{},{}'.format(toe_reading, first_mid_reading, second_mid_reading, ankle_reading)+EOL)

    sleep(DATA_RATE)
