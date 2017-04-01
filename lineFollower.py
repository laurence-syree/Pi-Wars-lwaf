""" this is a test script for developing the motorlibrary """
# Import built in libraries
import time
import os
import RPi.GPIO as GPIO
# Tabulate library is for creating the neat output tables
from tabulate import tabulate
# Import the motor library to power the motors
import motorLibrary

# Small function to check the values from the line following sensors
def checkSensor(pin):
	GPIO.setup(pin, GPIO.IN)
	# Return sensor value, True = Black, False = White
	return not GPIO.input(pin)

# Pins used to control direction of each motor
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

# Pins used to set speed of the motors
PWMS = {
	"l" : 16,
	"r" : 18
}

# Pin set for the line following sensors
linePins = {
	"l" : 15,
	"c" : 13,
	"r" : 11
}

# Set initial values so the debug info doesnt bug out on startup
scriptStatus = "Waiting for first result"
motion = {
	"left" : 0.5,
	"right" : 0.5
}

# Create an instanct of the motor library
MOTORS = motorLibrary.management(PINS, PWMS)

# Start a constant loop to keep the robot moving
while True:
	# Open a try statement to allow for clean exit
	try:
		# Get the values from the sensors and store the data
		left = checkSensor(linePins['l'])
		center = checkSensor(linePins['c'])
		right = checkSensor(linePins['r'])

		# Controls for harcoding the directions (Motor Testing)
		# left = False
		# center = True
		# right = False

		# Default the waiting to False until it is set later
		waitingBool = False

		# There is an if statement for every option the sensors could see (Except all at once and none at all)
		if left and not center and not right:
			# Set the status text for the debugging and the motion values for what you want the motors to do
			scriptStatus = "Left Only"
			motion = {
				"left" : 0.8,
				"right" : -0.4
			}
		elif left and center and not right:
			scriptStatus = "Left and Center"
			motion = {
				"left" : 0.8,
				"right" : -0.4
			}
		elif not left and not center and right:
			scriptStatus = "Right Only"
			motion = {
				"left" : -0.4,
				"right" : 0.8
			}
		elif not left and center and right:
			scriptStatus = "Center and Right"
			motion = {
				"left" : -0.4,
				"right" : 0.8
			}
		elif not left and center and not right:
			scriptStatus = "Center only"
			motion = {
				"left" : 0.4,
				"right" : 0.4
			}
		else:
			# If all the sensors or none of the triggers are being tripped set waiting to true
			waitingBool = True

		# Action the motion values defined above
		motorLeft, motorRight = MOTORS.move(motion["left"], motion["right"])
		time.sleep(0.07)
		# Pause then stop the motors
		MOTORS.stop()
		time.sleep(0.07)

		with open("log.txt", "a") as file1:
			file1.write(str(left) + str(center) + str(right) + "\n")

		# Display Debug Information using the tabulate library
		os.system("clear")
		print (tabulate([
			["status", scriptStatus],
			["waiting", str(waitingBool)],
			["Left Motor Setting", str(motion.get("left"))],
			["Right Motor Setting", str(motion.get("right"))],
			["Motor Actions"],
			["Left Motor", str(motorLeft)],
			["Right Motor", str(motorRight)],
			["Sensors"],
			["Left Sensor", str(left)],
			["Center Sensor", str(center)],
			["Right Sensor", str(right)]

			], tablefmt="fancy_grid"))

	# If the Ctrl+C hotkey is found end the loop and cleanup
	except KeyboardInterrupt:
		# Clean exiting for motor stopping
		MOTORS.stop()
		MOTORS.cleanup()

		# Display Debug Information using the tabulate library
		os.system("clear")
		print ("Keyboard interrupt detected, Last known status:")
		print (tabulate([
			["status", scriptStatus],
			["waiting", str(waitingBool)],
			["Left Motor Setting", str(motion.get("left"))],
			["Right Motor Setting", str(motion.get("right"))],
			["Motor Actions"],
			["Left Motor", str(motorLeft)],
			["Right Motor", str(motorRight)],
			["Sensors"],
			["Left Sensor", str(left)],
			["Center Sensor", str(center)],
			["Right Sensor", str(right)]

			], tablefmt="fancy_grid"))
		print ("Exiting")

		# Quit program
		exit(0)
