""" this is a test script for developing the motorlibrary """
# Next line is for the sublime pylinter plugin
# pylint: disable = I0011, C0103, R0201, C0330, C0103
import time
import MotorLibrary
import LineSenseLib
import progressbar

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
linePins = {
	"l" : 11,
	"c" : 13,
	"r" : 15
}

PWMS = {
	"l" : 18,
	"r" : 16
}

MOTORS = MotorLibrary.Management(PINS, PWMS)

motion = {
	"left" : 0.2,
	"right" : 0.2
}




while True:
	if LineSenseLib.checkSensor(linePins['c']) and not LineSenseLib.checkSensor(linePins['l']) and LineSenseLib.checkSensor(linePins['r']):
		motion = {
			"left" : 0.4,
			"right" : -0.4
		}
		print "1"
	elif LineSenseLib.checkSensor(linePins['c']) and LineSenseLib.checkSensor(linePins['l']) and not LineSenseLib.checkSensor(linePins['r']):
		motion = {
			"left" : -0.4,
			"right" : 0.4
		}
		print "2"
	elif LineSenseLib.checkSensor(linePins['c']) and not LineSenseLib.checkSensor(linePins['l']) and not LineSenseLib.checkSensor(linePins['r']):
		motion = {
			"left" : 0.05,
			"right" : 0.05
		}
		print "3"
	elif not LineSenseLib.checkSensor(linePins['c']) and LineSenseLib.checkSensor(linePins['l']) and not LineSenseLib.checkSensor(linePins['r']):
		motion = {
			"left" : -0.5,
			"right" : 0.5
		}
		print "4"
	elif not LineSenseLib.checkSensor(linePins['c']) and not LineSenseLib.checkSensor(linePins['l']) and LineSenseLib.checkSensor(linePins['r']):
		motion = {
			"left" : 0.5,
			"right" : -0.5
		}
		print "5"

	print motion
	# bar = progressbar.ProgressBar(maxval=20, \
	#     widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	# bar.start()
	# for i in xrange(20):
	#     bar.update(i+1)
	#     sleep(0.1)
	# bar.finish()
	MOTORS.move(motion["left"], motion["right"])
	time.sleep(0.05)
	MOTORS.stop()
	time.sleep(0.01)

# MOTORS.move(1, 1)
# time.sleep(1)
# MOTORS.move(-1, -1)
# time.sleep(1)
# MOTORS.move(1, -1)
# time.sleep(1)


MOTORS.stop()
MOTORS.cleanup()

