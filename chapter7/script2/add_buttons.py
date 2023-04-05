from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from oled import Write, GFX, SSD1306_I2C
import time

# write something on the OLED and wait 1 second
oled.text("It works!", 0, 0)
oled.show()
time.sleep(1)

# create dictionary to set up pins
buttons = {
    "button1": Pin(5, Pin.IN, Pin.PULL_UP),
    "button2": Pin(4, Pin.IN, Pin.PULL_UP),
    "button3": Pin(3, Pin.IN, Pin.PULL_UP),
    "button4": Pin(2, Pin.IN, Pin.PULL_UP)
    }

while True:
	# Clear the screen
    oled.fill(0)
    
    if buttons['button1'].value() == 0:
        oled.text("Button 1 pressed", 0, 0)
    elif buttons['button2'].value() == 0:
        oled.text("Button 2 pressed", 0, 0)
    elif buttons["button3"].value() == 0:
        oled.text("Button 3 pressed", 0,0)
    elif buttons['button4'].value() == 0:
        oled.text('Button 4 pressed', 0, 0)
    
    # update the display
    oled.show()
    time.sleep(1)
