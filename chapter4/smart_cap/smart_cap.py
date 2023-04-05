import board
import neopixel
import time
import touchio

pixel_pin = board.A1
num_of_pixels = 2

pixels = neopixel.NeoPixel(pixel_pin, num_of_pixels)

touch_pad_left = board.A0
touch_pad_right = board.A2
touch_left = touchio.TouchIn(touch_pad_left)
touch_right = touchio.TouchIn(touch_pad_right)

while True:
    if touch_left.value:
        pixels[0] = (0,0,255)
        pixels[1] = (0,0,255)
    elif touch_right.value:
        pixels[0] = (255,0,0)
        pixels[1] = (255,0,0)
    else:
        pixels[0] = (0,0,0) # off
        pixels[1] = (0,0,0)
