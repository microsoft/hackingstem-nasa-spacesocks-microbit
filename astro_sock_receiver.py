# ------------__ Hacking STEM astro_socks_receiver.py micro:bit __-----------
#  For use with the Astro Socks lesson plan available from 
#  Microsoft Education Workshop at http://aka.ms/hackingSTEM
#
#  Overview: This project relays incoming data from radio to serial
#  
#  To set radio channel, hold both buttons for 1 second and then use 
#  buttons to increment/decrement channel. See astro_socks.py 
#  for the companion transmitter program.
#
#  This project uses a BBC micro:bit microcontroller, information at:
#  https://microbit.org/
#
#  Comments, contributions, suggestions, bug reports, and feature
#  requests are welcome! 
#
#  Copyright 2019, Jeremy Franklin-Ross & Adi Azulay
#  Microsoft EDU Workshop - HackingSTEM
#  MIT License terms detailed in LICENSE.txt
# ===---------------------------------------------------------------===

from microbit import *
import radio

COMMA_COUNT = 4 # Count of expected commas for data integrity
EOL = '\n' # End of Line Character
chan = 0 # Defualt channel number for radio

display.off()  # Turns off LEDs to free up additional input pins
uart.init(baudrate=9600)  # Sets serial baud rate

radio.on() # Turns on radio
radio.config(length=64, channel=chan)

while True:    
    elapsed_buttons_down_millis = 0  # Reset button timer state 
    start_buttons_down_millis = running_time() # Reset button timer

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
            
    # Listen for radio data
    data_in = radio.receive()

	# Checksum of commas for incoming radio data
    if data_in and data_in.count(",") == COMMA_COUNT:
		uart.write(data_in + EOL)
