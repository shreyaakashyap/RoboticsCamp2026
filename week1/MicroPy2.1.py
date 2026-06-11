import machine
import utime

#led = machine.Pin('LED', machine.Pin.OUT)

ledRed = machine.Pin(11,machine.Pin.OUT)
ledYellow = machine.Pin(12,machine.Pin.OUT)
ledGreen = machine.Pin(13,machine.Pin.OUT)

i = int(input("Cycle Number?"))
while i>0:
    
    #led.value(1)
    ledGreen.value(1)
    utime.sleep(5)
    ledGreen.value(0)
    
    ledYellow.value(1)
    utime.sleep(1)
    ledYellow.value(0)
    
    #led.value(0)
    ledRed.value(1)
    utime.sleep(3)
    ledRed.value(0)
    
    i -= 1
    
    
    
