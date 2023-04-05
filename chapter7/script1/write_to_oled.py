from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from oled import Write, GFX, SSD1306_I2C

# set up I2C pins connected to OLED
i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=200000)

# create OLED object
oled = SSD1306_I2C(128, 32, i2c)

# write something on the OLED and wait 1 second
oled.text("It works!", 0, 20)
oled.show()
time.sleep(1)
