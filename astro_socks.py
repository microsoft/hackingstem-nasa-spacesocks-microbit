# ------------__ Hacking STEM astro_socks.py micro:bit __-----------===
#  For use with the Astro Socks lesson plan available from Microsoft 
#  Education Workshop at http://aka.ms/hackingSTEM
#
#  Overview: This project reads voltage on 4 GPIO pins and writes 
#  those values to serial and radio.
# 
#  Pins:
#  Pin 0 = Phalanges Sensor
#  Pin 1 = Metatarsals Sensor
#  Pin 2 = Tarsals Sensor
#  Pin 3 = Ankle Sensor
#  
#  How to get data:
#  You may connect this microbit to USB directly or use the companion
#  radio receiver program (astro_socks_receiver.py) to receive via
#  radio.
#
#  Channel select:
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

#=============================================================================#
#------------------------------Main Program Loop------------------------------#
#=============================================================================#
while (True):
    elapsed_buttons_down_millis = 0  # Reset button timer state
    start_buttons_down_millis = running_time()  # Reset button timer state

    # If both buttons have been held for over a second or 
    # both button are currently being pressed, stay in while loop
    while (elapsed_buttons_down_millis > 1000 and elapsed_buttons_down_millis < 11000) or (button_a.is_pressed() and button_b.is_pressed()):
        # check elapsed time
        elapsed_buttons_down_millis = running_time() - start_buttons_down_millis

        # check elapsed time
        if elapsed_buttons_down_millis > 1000 and elapsed_buttons_down_millis < 11000:
            if not display.is_on():
                display.on()  

            # decrement if only button A is was or is pressed
            if (button_a.was_pressed() or button_a.is_pressed()) and chan != 0 and not button_b.is_pressed():
                chan -= 1
                radio.config(channel=chan)
            # increment if only button B is was or is pressed
            elif (button_b.was_pressed() or button_b.is_pressed()) and chan < 83 and not button_a.is_pressed():
                chan += 1
                radio.config(channel=chan)                
            display.show(chan, delay=250, wait=True)
            if chan > 9:
                display.show("_")
            sleep(250) 
            
    if display.is_on():
        display.off() 
            
    # Read from each sensor
    phalanges_reading = pin0.read_analog()
    metatarsals_reading = pin1.read_analog()
    tarsals_reading = pin2.read_analog()
    ankle_reading = pin3.read_analog()

    # Create a string of the data to be sent
    data_to_send = ",{},{},{},{}".format(phalanges_reading, metatarsals_reading, tarsals_reading, ankle_reading)

    # Send data to radio
    radio.send(data_to_send)

    # Also write out to Serial (so you can use radio or serial)
    # uart is the micro:bit command for serial
    uart.write(data_to_send + EOL)

    sleep(DATA_RATE)
