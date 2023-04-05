# set up radio
import radio
radio.config(channel=10)
radio.on()

from microbit import *

pin16.write_digital(0)  # start with the pump off

while True:
    soil = pin1.read_analog()  # read moisture
    radio.send(str(soil))   # send moisture over radio to receiving microbit
    if soil > 500:
        display.show(Image.HAPPY)
        pin16.write_digital(0)  # turn off the pump
    else:
        display.show(Image.SAD)
        pin16.write_digital(1)  # turn on the pump
