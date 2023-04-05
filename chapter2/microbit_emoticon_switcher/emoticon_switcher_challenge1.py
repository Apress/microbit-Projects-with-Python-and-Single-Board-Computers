from microbit import *
import radio

# Create a dictonary of our emoticon images
images = {
    1: Image.HEART,
    2: Image.HEART_SMALL,
    3: Image.HAPPY,
    4: Image.SAD,
    5: Image.SURPRISED,
    6: Image.ANGRY,
    7: Image.ASLEEP,
    8: Image.BUTTERFLY,
    9: Image.DIAMOND,
    10: Image.CONFUSED,
    11: Image.COW,
    12: Image.PACMAN,
}
index_num = 1

# Set the radio channel to 10
radio.config(channel=10)
radio.on()

while True:
    # Capture received radio data
    incoming = radio.receive()

    # check for tilting and change index_num
    x_tilt = accelerometer.get_x()
    if x_tilt > 400:
        index_num += 1
    if x_tilt < -400:
        index_num -= 1

    # Send the current emoticon if both buttons pressed together
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send(str(index_num))
        display.show("sending...")

    # If there's incoming data, show the emoticon that's been received
    if incoming:
        display.show(Image.TARGET)
        sleep(500)
        display.show(images[int(incoming)])
        sleep(2000)

    # Keep the index_num within the valid dictionary key range
    if index_num > 12:
        index_num = 1
    elif index_num < 1:
        index_num = 12

    # Show the current image
    display.show(images[index_num])
    sleep(500)
