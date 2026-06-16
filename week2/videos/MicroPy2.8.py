import machine
import utime

switch = machine.Pin(14, machine.Pin.IN)

while True:
    if switch.value() == 1:
        print("The switch is pressed!")
        utime.sleep(0.5)  # Debounce delay