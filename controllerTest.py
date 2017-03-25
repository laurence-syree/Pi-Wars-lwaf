""" Script to pull information from a controller and pass on motor control information """
# Next line is for the sublime pylinter plugin
# pylint: disable = I0011, C0103, R0201, C0330, C0103
import math
import motorLibrary
import os
import time
from evdev import InputDevice, list_devices, categorize, ecodes, RelEvent



PINS = {
    "frf" : 40,
    "frb" : 38,
    "flf" : 32,
    "flb" : 36,
    "brf" : 37,
    "brb" : 35,
    "blf" : 22,
    "blb" : 33
}

PWMS = {
    "l" : 16,
    "r" : 18
}

motion = {
    "left" : 0.5,
    "right" : 0.5
}


MOTORS = motorLibrary.management(PINS, PWMS)

def clamp(my_value, min_value, max_value):
    return max(min(my_value, max_value), min_value)

button = {}

    # these are the identifiers for the PS4's accelerometers
AXIS_X = 3
AXIS_Y = 4

    # variables we'll store the rotations in, initialised to zero
rot_x = 0.0
rot_y = 0.0
forwardDown = False
backwardsDown = False
headingX = 0
forwardTrigger = 0
backwardsTrigger = 0

found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == 'Wireless Controller':
        found = True;
        print("Found")
        break
if not(found):
  print('Device not found. Aborting ...')
  exit()

def move(direction, magnitude):

    direction *= 1.9;

    if direction <= 0:
        leftValue = magnitude
        rightValue = magnitude - abs(direction)*magnitude
    else:
        leftValue = magnitude - abs(direction)*magnitude
        rightValue = magnitude

    leftValue = round(leftValue, 2)
    rightValue = round(rightValue, 2)

    print(str(leftValue) + " : " + str(rightValue))
    MOTORS.move(leftValue, rightValue)

lastUpdate = 0

def getTime():
    return int(round(time.time() * 1000))

try:

    # main loop
    while True:
        
        try:

            for event in dev.read():

                if event.type == ecodes.EV_KEY:

                    if event.code == 311:
                        forwardDown = event.value

                        if not forwardDown:
                            MOTORS.stop()

                    if event.code == 310:

                        backwardsDown = event.value

                        if not backwardsDown:
                            MOTORS.stop()

                    if event.code == 308:
                        if event.value:
                            MOTORS.move(-1, 1)
                        else:
                            MOTORS.stop()

                    if event.code == 309:
                        if event.value:
                            MOTORS.move(1, -1)
                        else:
                            MOTORS.stop()

                if event.type == ecodes.EV_ABS:
                    if event.code in ecodes.ABS:
                        symbol = ecodes.ABS[event.code]

                        if symbol == "ABS_X":
                            headingX = (event.value-130) / 255.0

                        if symbol == "ABS_RY":
                            scale = event.value / 255.0
                            forwardTrigger = scale

                        if symbol == "ABS_RX":
                            scale = event.value / 255.0
                            backwardsTrigger = scale

        except IOError:
            pass

        if getTime()-lastUpdate > 10:
            if forwardDown and forwardTrigger > 0.1:
                move(headingX, forwardTrigger)
            elif backwardsDown and backwardsTrigger > 0.1:
                move(headingX, -backwardsTrigger)

            lastUpdate = getTime()

except KeyboardInterrupt:
        # Clean exiting for motor stopping
        MOTORS.stop()
        MOTORS.cleanup()

        # Display Debug Information
        os.system("clear")
        print ("Keyboard interrupt detected, Last known status:")
        print ("Exiting")

        # Quit program
        exit(0)
