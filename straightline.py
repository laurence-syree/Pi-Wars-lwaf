import motorLibrary
import time
import os

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

MOTORS = motorLibrary.management(PINS, PWMS)
MOTORS.move(1, 1)

try:

    # main loop
    while True:
    	time.sleep(0.1)

except KeyboardInterrupt:
        # Clean exiting for motor stopping
        MOTORS.stop()
        MOTORS.cleanup()

        # Display Debug Information
        os.system("clear")
        print ("Keyboard interrupt detected, Last known status:")
        print ("Exiting")

        # Quit program
        exit(0)
