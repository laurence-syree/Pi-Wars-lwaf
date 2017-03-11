""" this is a test script for developing the motorlibrary """
# Next line is for the sublime pylinter plugin
# pylint: disable = I0011, C0103, R0201, C0330, C0103
import time, os
import motorLibrary, lineFollower

# System setup
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

linePins = {
	"l" : 11,
	"c" : 13,
	"r" : 15
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
		waitingBool = False

		if left and not center and not right:
			scriptStatus = "Left Only"
			motion = {
				"left" : 0.2,
				"right" : 0.8
			}
		elif left and center and not right:
			scriptStatus = "Left and Center"
			motion = {
				"left" : 0.2,
				"right" : 0.8
			}
		elif not left and not center and right:
			scriptStatus = "Right Only"
			motion = {
				"left" : 0.8,
				"right" : 0.2
			}
		elif not left and center and right:
			scriptStatus = "Center and Right"
			motion = {
				"left" : 0.8,
				"right" : 0.2
			}
		elif not left and center and not right:
			scriptStatus = "Center only"
			motion = {
				"left" : 0.5,
				"right" : 0.5
			}
		else:
			waitingBool = True

		motorLeft, motorRight = MOTORS.move(motion["left"], motion["right"])
		time.sleep(0.15)
		MOTORS.stop()
		time.sleep(0.01)

		# Display Debug Information
		os.system("clear")
		print ("status : " + scriptStatus)
		for key, value in motion.items():
			print (str(key) + " : " + str(value))
		print ("waiting : " + str(waitingBool))
		print ("\nLeft Motor : " + str(motorLeft))
		print ("Right Motor : " + str(motorRight))

	except KeyboardInterrupt:
		# Clean exiting for motor stopping
		MOTORS.stop()
		MOTORS.cleanup()

		# Display Debug Information
		os.system("clear")
		print ("Keyboard interrupt detected, Last known status:")
		print ("status : " + scriptStatus)
		for key, value in motion.items():
			print (str(key) + " : " + str(value))
		print ("waiting : " + str(waitingBool))
		print ("\nLeft Motor : " + str(motorLeft))
		print ("Right Motor : " + str(motorRight))
		print ("Exiting")

		# Quit program
		exit(0)
