from microbit import *
import radio
    
radio.config(channel=1)
radio.on()
while True:
  received_data = radio.receive()
  if received_data:
    print(int(received_data))
