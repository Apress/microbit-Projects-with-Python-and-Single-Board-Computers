from microbit import *

def stopBit(colour):
    if colour == "green":
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(1)
    elif colour == "amber":
        pin0.write_digital(0)
        pin1.write_digital(1)
        pin2.write_digital(0)
    elif colour == "red":
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)

# main loop
while True:
    stopBit("green")
    sleep(5000)
    stopBit("amber")
    sleep(5000)
    stopBit("red")
    sleep(5000)
