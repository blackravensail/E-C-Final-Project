import board
from time import sleep
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn

switch = DigitalInOut(board.D4)
switch.direction = Direction.INPUT

switch.pull = Pull.Up

in_pin = AnalgoIn(board.A1)

while True:
    if not switch.value:
        print(f"{3.3*in_pin.value/65535}V")
        sleep(0.5)
    

