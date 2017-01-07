import os
import RPi.GPIO as GPIO
from time import sleep

def MoveBy(direction, distance):
	#Set the mode for the GPIO pin referencing
	GPIO.setmode(GPIO.BCM)
	#Define the forward and backward GPIO pins for the DC motor
	ForwardPin = 9
	BackwardPin = 10

	# Setup the GPIO pins ready for control
	GPIO.setup(ForwardPin,GPIO.OUT)
	GPIO.setup(BackwardPin,GPIO.OUT)

	# Based on direction set the required direction pin to high
	if direction == "f":
		GPIO.output(ForwardPin, GPIO.HIGH)
	elif direction == "b":
		GPIO.output(BackwardPin, GPIO.HIGH)
	else:
		# If invalid direction throw error
		raise ValueError("Invalid direction specified", direction)

	try:
		sleep(float(distance))
	except:
		# Set all GPIO pins to low to kill any movement
		GPIO.output(ForwardPin, GPIO.LOW)
		GPIO.output(BackwardPin, GPIO.LOW)
		# If invalid distance throw error
		raise ValueError("Invalid Distance Specified", distance)
		# Release hold on GPIO pins
		GPIO.cleanup()

	# Set all GPIO pins to low to kill any movement
	GPIO.output(ForwardPin, GPIO.LOW)
	GPIO.output(BackwardPin, GPIO.LOW)

	# Release hold on GPIO pins
	GPIO.cleanup()

def Turn(direction):
	# Based on the specified direction send the signal to the servo to turn
	if direction == "r":
		os.system("echo 0=25% > /dev/servoblaster")
	elif direction == "l":
		os.system("echo 0=75% > /dev/servoblaster")
	elif direction == "s":
		os.system("echo 0=50% > /dev/servoblaster")
	else:
		# Raise direction invalid error
		raise ValueError("Invalid Direction Specified", direction)