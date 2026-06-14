import machine
import utime

red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

def map_value(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def set_color(r, g, b):
    red.duty_u16(map_value(r, 0, 255, 0, 65535))
    green.duty_u16(map_value(g, 0, 255, 0, 65535))
    blue.duty_u16(map_value(b, 0, 255, 0, 65535))

colors = [
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (0, 255, 255),   # Cyan
    (255, 0, 255),   # Magenta
    (255, 255, 255)  # White
]

while True:
    for color in colors:
        set_color(*color)
        utime.sleep(1)
