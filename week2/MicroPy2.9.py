import machine
import utime

reed_switch = machine.Pin(14, machine.Pin.IN)

while True:
    if reed_switch.value() == 1:
        print("Magnet detected!")
        utime.sleep(1) 