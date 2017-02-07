import os
import sys
import RPi.GPIO as GPIO
from time import sleep

direction = raw_input("For forwards put 'f' for backwards put 'b' : ") 
time = raw_input("How long would you like the robot to run for /seconds : ")

GPIO.setmode(GPIO.BCM)

ForwardPinA = 23
BackwardPinA = 24
ForwardPinB = 10
BackwardPinB = 9

# Setup the GPIO pins ready for control
GPIO.setup(ForwardPinA,GPIO.OUT)
GPIO.setup(BackwardPinA,GPIO.OUT)
GPIO.setup(ForwardPinB,GPIO.OUT)
GPIO.setup(BackwardPinB,GPIO.OUT)

print "Turning motor on"

if direction == "f":
	GPIO.output(ForwardPinA, GPIO.HIGH)
	GPIO.output(ForwardPinB, GPIO.HIGH)
else:
	GPIO.output(BackwardPinA, GPIO.HIGH)
	GPIO.output(BackwardPinB, GPIO.HIGH)

sleep(float(time))

print "Stopping motor"
# Set all GPIO pins to low to kill any movement
GPIO.output(ForwardPinA, GPIO.LOW)
GPIO.output(BackwardPinA, GPIO.LOW)
GPIO.output(ForwardPinB, GPIO.LOW)
GPIO.output(BackwardPinB, GPIO.LOW)

# Release hold on GPIO pins
GPIO.cleanup()


# echo 0=50% > /dev/servoblaster
# echo 0=-20 > /dev/servoblaster
# echo 0=+20 > /dev/servoblaster
