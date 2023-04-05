from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from oled import Write, GFX, SSD1306_I2C
import time, dht

# create dictionary to set up pins
buttons = {
    "button1": Pin(5, Pin.IN, Pin.PULL_UP),
    "button2": Pin(4, Pin.IN, Pin.PULL_UP),
    "button3": Pin(3, Pin.IN, Pin.PULL_UP),
    "button4": Pin(2, Pin.IN, Pin.PULL_UP)
    }

# set up DHT11 data pin
dsensor = dht.DHT11(Pin(18))

# set up LED output pin and switch off
led1 = Pin(0, Pin.OUT)
led1.low()

# set up I2C pins connected to OLED
i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=200000)

# create OLED object
oled = SSD1306_I2C(128, 32, i2c)

# write something on the OLED and wait 2 secs.
oled.text("It works!", 0, 0)
oled.show()
time.sleep(1)

while True:
    oled.fill(0)
    try:
        dsensor.measure()
    except:
        print('error reading') # in case reading fails keep running

    if buttons['button1'].value() == 0:
        oled.text("Button 1 pressed", 0, 0)
        oled.text("Temperature: "+str(dsensor.temperature())+"C", 0, 20)
    elif buttons['button2'].value() == 0:
        oled.text("Button 2 pressed", 0, 0)
        oled.text("Humidity: "+str(dsensor.humidity())+"%", 0, 20)
    elif buttons["button3"].value() == 0:
        oled.text("Button 3 pressed", 0,0)
        oled.text('LED switched ON!', 0, 20)
        led1.high()
    elif buttons['button4'].value() == 0:
        oled.text('Button 4 pressed', 0, 0)
        oled.text('LED switched OFF!', 0, 20)
        led1.low()
    else:
        oled.text("-Menu-", 0, 0)
        oled.text("1. Temperature", 0, 7)
        oled.text("2. Humidity", 0, 16)
        oled.text("3/4. LED switch", 0, 25)
    # update the display
    oled.show()
    time.sleep(1)
