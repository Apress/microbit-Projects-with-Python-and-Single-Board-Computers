from microbit import *
while True:
   soil = pin1.read_analog()
   print(soil)
   # we can start at 500 but you will need to work out the best soil value
   if soil > 500:
       display.show(Image.HAPPY)
   else:
       display.show(Image.SAD)
