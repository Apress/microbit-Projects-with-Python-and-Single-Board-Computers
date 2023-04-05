from microbit import *
from stopbit import stopBit

import radio
radio.on()
radio.config(channel=7)

while True:
    stopBit("green") # state 1
    radio.send("red")
    sleep(5000)
    stopBit("amber") # state 2
    radio.send("red")
    sleep(2500)
    stopBit("red") # state 3
    radio.send("green")
    sleep(2500)
    stopBit("red") # state 4
    radio.send("amber")
    sleep(2500)
