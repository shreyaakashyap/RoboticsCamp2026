import machine
import utime
import random

pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
leds = []

for pin_number in pins:
    led = machine.Pin(pin_number, machine.Pin.OUT)
    leds.append(led)

#Pattern 1
#while True:
 #   
  #  for led in leds:
   #     led.value(1) 
    #    utime.sleep(0.2)
    
   # for led in leds:
    #    led.value(0) 
     #   utime.sleep(0.2)
        
#Pattern 2
#while True:
 #   
  #  for led in leds:
   #     led.value(1) 
    #    utime.sleep(0.2)
    #
    #for led in reversed(leds):
     #   led.value(0) 
      #  utime.sleep(0.2)
        
#Pattern 3
#while True:
 #   
  #  for led in reversed(leds):
   #     led.value(1) 
    #    utime.sleep(0.2)
    #
    #for led in leds:
     #   led.value(0) 
      #  utime.sleep(0.2)
        
#Pattern 4
#while True:
    
 #   for led in reversed(leds):
  #      led.value(1) 
   #     utime.sleep(0.2)
    
    #for led in reversed(leds):
     #   led.value(0) 
      #  utime.sleep(0.2)
        
#Pattern 5
while True:
    
    ledRandom = random.choice(leds)
    ledRandom.value(1)
    utime.sleep(0.2)
    ledRandom.value(0)