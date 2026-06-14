import machine
import utime

led = machine.PWM(machine.Pin(15))
led.freq(100)  

while True:
    for duty in range(0, 65536, 256):
        led.duty_u16(duty)  
        utime.sleep(0.1)   

        led.duty_u16(0)