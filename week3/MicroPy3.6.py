import machine
import utime

# Define the control pins connected to the TA6586
motor1A = machine.Pin(14, machine.Pin.OUT)
motor2A = machine.Pin(15, machine.Pin.OUT)

# Start the pump by setting motor1A high and motor2A low
while True:
    motor1A.high()
    motor2A.low()