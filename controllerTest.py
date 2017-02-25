""" Script to pull information from a controller and pass on motor control information """
# Next line is for the sublime pylinter plugin
# pylint: disable = I0011, C0103, R0201, C0330, C0103
import pygame
import math
import MotorLibrary
import os

PINS = {
    "frf" : 33,
    "frb" : 22,
    "flf" : 37,
    "flb" : 35,
    "brf" : 32,
    "brb" : 36,
    "blf" : 40,
    "blb" : 38
}

PWMS = {
    "l" : 18,
    "r" : 16
}

MOTORS = MotorLibrary.Management(PINS, PWMS)
MOTORS.stop()


def clamp(my_value, min_value, max_value):
    return max(min(my_value, max_value), min_value)

pygame.init()
pygame.joystick.init()

controller = pygame.joystick.Joystick(0)
controller.init()

screen = pygame.display.set_mode((100, 100))


axis = {}
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

def move(direction, magnitude):

    print("steer: " + str(round(direction, 2)))
    print("trig: " + str(round(magnitude, 2)))


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


    # main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            button[event.button] = True

            if event.button == 7:
                # R2
                forwardDown = True
            if event.button == 6:
                # L2
                backwardsDown = True
            if event.button == 5:
                # R1
                print "right"
                MOTORS.move(1, -1)
            if event.button == 4:
                # L1
                print "left"
                MOTORS.move(-1, 1)
            if event.button == 8:
                # Share
                print "Shut down"
                os.system("shutdown -h now")
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 7:
                forwardDown = False
                MOTORS.stop()
            if event.button == 6:
                backwardsDown = False
                MOTORS.stop()
            if event.button == 5:
                # R1
                MOTORS.stop()
            if event.button == 4:
                # L1
                MOTORS.stop()

        if event.type == pygame.JOYHATMOTION:
            print("hat")

        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                headingX = event.value

            if event.axis == 4:
                scale = (event.value + 1) / 2
                forwardTrigger = scale

            if event.axis == 5:
                scale = (event.value + 1) / 2
                backwardsTrigger = scale

        if forwardDown:
            move(headingX, forwardTrigger)
        elif backwardsDown:
            move(headingX, -backwardsTrigger)

            


