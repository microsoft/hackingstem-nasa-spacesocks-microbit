# Introduction
Micropython code for HackingSTEM Astro Socks lesson plan adapted for micro:bit


**Note** that this project is designed to use 2 micro:bits since each board only supports up to 6 analog/pwm pins. It also allows for wireless testing.
* astro_socks.py
Captures the analog signals from the flex sensors and transmits this data over radio to the receiver micro:bit
* astro_socks_receiver.py
Receives data from the Gloastro_sock micro:bit and controls the servos in the mechanical hand. This one attaches to your laptop.

Both micro:bits must be on the same radio channel for this to work. To change the channel press both buttons until a number appears. This is the channel number. Set this to the same number on each micro:bit. If there are multiple projects going on in the same room choose a unique channel number for each astro_sock/receiver pair. It is also possible to for the receiver to cycle through each channel on a single receiver laptop.

# Getting Started
1. Download lesson assets at https://aka.ms/astrosocks
1. Assemble your electronics
1. Use [Mu](https://codewith.mu/) to flash astro_socks.py [micro:bit](https://microbit.org/) sensor microcontroller
1. Use [Mu](https://codewith.mu/) to flash astro_socks_receiver.py to your receiver [micro:bit](https://microbit.org/) microcontroller
1. Verify data interactions in Excel from (hand microcontroller)
1. Ready, Set, Science!

# Microsoft Data Streamer Resources
1. https://aka.ms/data-streamer-developer
1. https://aka.ms/data-streamer

# Make it your own!
This project is licensed under the MIT open source license, see License. The MIT license allows you to take this project and make awesome things with it! MIT is a very permissive license, but does require you include license and copyright from LICENSE in any derivative work for sake of attribution.

Fork away! Let us know what you build!

http://aka.ms/hackingSTEM
