import os
import sys
import RPi.GPIO as GPIO
from time import sleep

direction = raw_input("For forwards put 'f' for backwards put 'b' : ") 
time = raw_input("How long would you like the robot to run for /seconds : ")

GPIO.setmode(GPIO.BCM)

ForwardPin = 9
BackwardPin = 10

# Setup the GPIO pins ready for control
GPIO.setup(ForwardPin,GPIO.OUT)
GPIO.setup(BackwardPin,GPIO.OUT)

print "Turning motor on"

if direction == "f":
	GPIO.output(ForwardPin, GPIO.HIGH)
else:
	GPIO.output(BackwardPin, GPIO.HIGH)

sleep(float(time))

print "Stopping motor"
# Set all GPIO pins to low to kill any movement
GPIO.output(ForwardPin, GPIO.LOW)
GPIO.output(BackwardPin, GPIO.LOW)

# Release hold on GPIO pins
GPIO.cleanup()


# echo 0=50% > /dev/servoblaster
# echo 0=-20 > /dev/servoblaster
# echo 0=+20 > /dev/servoblaster
