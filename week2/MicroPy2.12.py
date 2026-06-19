import machine
import utime

photoresistor = machine.ADC(28)

while True:
    light_value = photoresistor.read_u16()
    print("Light value:", light_value)
    utime.sleep(0.5)