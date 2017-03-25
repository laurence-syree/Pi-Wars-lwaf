""" this is a test script for developing the motorlibrary """
# Next line is for the sublime pylinter plugin
# pylint: disable = I0011, C0103, R0201, C0330, C0103
print ("control, pre import")
import time
print ("1")
import os
print ("2")
import motorLibrary
print ("3")
import lineFollower
print ("4")
from tabulate import tabulate
print ("control, post import")

# System setup
PINS_bk = {
	"frf" : 33,
	"frb" : 22,
	"flf" : 37,
	"flb" : 35,
	"brf" : 32,
	"brb" : 36,
	"blf" : 40,
	"blb" : 38
}

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

linePins = {
	"l" : 15,
	"c" : 13,
	"r" : 11
}

scriptStatus = "Waiting for first result"
motion = {
	"left" : 0.5,
	"right" : 0.5
}

MOTORS = motorLibrary.management(PINS, PWMS)

while True:
	try:
		left = lineFollower.checkSensor(linePins['l'])
		center = lineFollower.checkSensor(linePins['c'])
		right = lineFollower.checkSensor(linePins['r'])
		# left = False
		# center = True
		# right = False

		waitingBool = False

		if left and not center and not right:
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
			waitingBool = True

		motorLeft, motorRight = MOTORS.move(motion["left"], motion["right"])
		time.sleep(0.07)
		MOTORS.stop()
		time.sleep(0.07)

		# Display Debug Information
		os.system("clear")
		# print ("status : " + scriptStatus)
		# for key, value in motion.items():
		# 	print (str(key) + " : " + str(value))
		# print ("waiting : " + str(waitingBool))
		# print ("\nLeft Motor : " + str(motorLeft))
		# print ("Right Motor : " + str(motorRight))
		# print (str(left) + str(center) + str(right) + "\n\n\n\n")
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

	except KeyboardInterrupt:
		# Clean exiting for motor stopping
		MOTORS.stop()
		MOTORS.cleanup()


		# Display Debug Information
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
