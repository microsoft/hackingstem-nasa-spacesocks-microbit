# ------------__ Hacking STEM astro_socks.py micro:bit __-----------
#  For use with the Astro Socks lesson plan available from 
#  Microsoft Education Workshop at http://aka.ms/hackingSTEM
#
#  Overview: This project reads voltage on 4 GPIO pins and writes those values
#  to serial and radio.
# 
#  Pins:
#  Pin 0 = Phalanges Sensor
#  Pin 1 = Metatarsals Sensor
#  Pin 2 = Tarsals Sensor
#  Pin 3 = Ankle Sensor
#  
#  To set radio channel, hold both buttons for 1 second and then use 
#  buttons to increment/decrement channel. See astro_socks_receiver.py 
#  for the companion receiver program.
#
#  This project uses a BBC micro:bit microcontroller, information at:
#  https://microbit.org/
#
#  Comments, contributions, suggestions, bug reports, and feature
#  requests are welcome! For source code and bug reports see:
#  http://github.com/microsoft/[TODO github path to Hacking STEM]
#
#  Copyright 2019, Jeremy Franklin-Ross & Adi Azulay
#  Microsoft EDU Workshop - HackingSTEM
#  MIT License terms detailed in LICENSE.txt
# ===---------------------------------------------------------------===

from microbit import *
import radio

# Setup & Config
display.off()  # Turns off LEDs to free up additional input pins
uart.init(baudrate=9600)  # Sets serial baud rate
DATA_RATE = 10 # Frequency of code looping
EOL = '\n' # End of Line Character
chan = 0 # Defualt channel number for radio
radio.config(length=64, channel=chan)
radio.on() # Turn on radio


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
#------------------------------Main Program Loop------------------------------#
#=============================================================================#
while (True):
    # Change radio channel
    elapsed_buttons_down_millis = 0
    start_buttons_down_millis = running_time() 
    while (elapsed_buttons_down_millis > 1000 and elapsed_buttons_down_millis < 11000) or (button_a.is_pressed() and button_b.is_pressed()):
        elapsed_buttons_down_millis = running_time() - start_buttons_down_millis
        if elapsed_buttons_down_millis > 1000 and elapsed_buttons_down_millis < 11000:
            if not display.is_on():
                display.on()  

            if (button_a.was_pressed() or button_a.is_pressed()) and chan != 0 and not button_b.is_pressed():
                chan -= 1
                radio.config(channel=chan)
            elif (button_b.was_pressed() or button_b.is_pressed()) and chan < 83 and not button_a.is_pressed():
                chan += 1
                radio.config(channel=chan)                
            display.show(chan, delay=250, wait=True)
            if chan > 9:
                display.show("_")
            sleep(250) 
            
    if display.is_on():
        display.off() 
            

    process_sensors()

    # Create a string of the data to be sent
    data_to_send = ",{},{},{},{}".format(toe_reading, first_mid_reading, second_mid_reading, ankle_reading)

    # Send data to radio
    radio.send(data_to_send)

    # uart is the micro:bit command for serial
    uart.write(data_to_send + EOL)

    sleep(DATA_RATE)
