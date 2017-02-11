import time
import MotorControl


# System setup
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

motors = MotorControl.management(pins, pwms)

motors.move(1, -1)

time.sleep(2)
motors.stop()
motors.cleanup()
