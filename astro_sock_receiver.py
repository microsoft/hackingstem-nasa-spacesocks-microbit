from microbit import *
import radio


DATA_SPEED = 10 # Frequency of code looping
COMMA_COUNT = 4 # Count of expected commas for data integrity
EOL = '\n' # End of Line Character
chan = 0 # Defualt channel number for radio

display.off()  # Turns off LEDs to free up additional input pins
uart.init(baudrate=9600)  # Sets serial baud rate

radio.on() # Turns on radio
radio.config(length=64, channel=chan)

while True:    
    # Changes the radio channel
    while button_a.is_pressed() and chan != 0:
        chan -= 1
        radio.config(channel=chan)
        display.on()
        display.show(chan, delay=500)
        sleep(600)
        display.off()
    while button_b.is_pressed() and chan < 83:
        chan += 1
        radio.config(channel=chan)
        display.on()
        display.show(chan, delay=500)
        sleep(600)
        display.off()
    
    # Listen for radio data
    data_in = radio.receive()

	# Seperate the incoming radio data
    if data_in and data_in.count(",") == COMMA_COUNT:
		uart.write(data_in + EOL)



