import machine
import utime

tilt_switch = machine.Pin(14, machine.Pin.IN)

while True:
    if tilt_switch.value() == 0:
        print("Tilt detected!\n--------------------")
        utime.sleep(1)  