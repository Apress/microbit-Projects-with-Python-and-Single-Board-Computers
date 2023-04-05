from microbit import *
from stopbit import stopBit
# this requires the stopbit.py file on the micro:bit

import radio
radio.on()
radio.config(channel=7)

while True:
    incoming = radio.receive()
    if incoming:
        stopBit(incoming)
