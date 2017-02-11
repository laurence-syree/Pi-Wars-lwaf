""" this is a test script for developing the motorlibrary """
# Next line is for the sublime pylinter plugin
# pylint: disable = I0011, C0103, R0201, C0330, C0103
import time
import MotorControl


# System setup
PINS = {
	   "frf" : 33,
	"frb" : 22,
	"flf" : 35,
	"flb" : 37,
	"brf" : 32,
	"brb" : 36,
	"blf" : 38,
	"blb" : 40
}

PWMS = {
	"l" : 18,
	"r" : 16
}

MOTORS = MotorControl.Management(PINS, PWMS)

motors.move(1, -1)

time.sleep(2)
MOTORS.stop()
MOTORS.cleanup()
