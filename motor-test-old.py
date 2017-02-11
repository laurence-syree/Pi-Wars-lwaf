import RPi.GPIO as GPIO
from time import sleep

direction = ""
while direction != "exit":
	direction = raw_input("Please enter the direction: ")
	speed = float(raw_input("Please enter the speed (25-90): "))

	pins = {
		"frf" : 33,
		"frb" : 22,
		"flf" : 35,
		"flb" : 37,
		"brf" : 32,
		"brb" : 36,
		"blf" : 38,
		"blb" : 40
	}

	pwms = {
		"l" : 18,
		"r" : 16
	}



	GPIO.setmode(GPIO.BOARD)
	# Setup the GPIO pins ready for control
	for key, pin in pins.items():
		GPIO.setup(pin,GPIO.OUT)

	# Start PWM for the right side of the robot
	GPIO.setup(pwms["r"], GPIO.OUT)
	p = GPIO.PWM(pwms["r"], 50)
	p.start(speed)

	# Start PWM for the left side of the robot
	GPIO.setup(pwms["l"], GPIO.OUT)
	p2 = GPIO.PWM(pwms["l"], 50)
	p2.start(speed)

	# Based on direction set the required direction pin to high
	if direction == "f":
		for key, pin in pins.items():
			if key.endswith('f'):
				GPIO.output(pin, GPIO.HIGH)

	elif direction == "b":
		for key, pin in pins.items():
			if key.endswith('b'):
				GPIO.output(pin, GPIO.HIGH)
				
	elif direction == "l":
		for key, pin in pins.items():
			if key[1] == 'l' and key.endswith('b'):
				GPIO.output(pin, GPIO.HIGH)
			if key[1] == 'r' and key.endswith('f'):
				GPIO.output(pin, GPIO.HIGH)

	elif direction == "r":
		for key, pin in pins.items():
			if key[1] == 'r' and key.endswith('b'):
				GPIO.output(pin, GPIO.HIGH)
			if key[1] == 'l' and key.endswith('f'):
				GPIO.output(pin, GPIO.HIGH)

	else:
		# If invalid direction throw error
		raise ValueError("Invalid direction specified", direction)

	try:
		sleep(float(distance))
	except:
		# Set all GPIO pins to low to kill any movement
		for key, pin in pins.items():
			GPIO.output(pins, GPIO.LOW)

		# If invalid distance throw error
		raise ValueError("Invalid Distance Specified", distance)
		# Release hold on GPIO pins
		GPIO.cleanup()

	# Set all GPIO pins to low to kill any movement
	for key, pin in pins.items():
		GPIO.output(pin, GPIO.LOW)

	p.stop()
	p2.stop()
	# Release hold on GPIO pins
	GPIO.cleanup()