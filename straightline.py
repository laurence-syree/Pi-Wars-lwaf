# Import the build in libraries for the script
import time
import os
# Import the motor library file which allows control of the motors
import motorLibrary

# Define the pins which will be used to drive the motors
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

# Define the pins which are used to manage the motor speed
PWMS = {
	"l" : 16,
	"r" : 18
}

# Create an instance of the motor library
MOTORS = motorLibrary.management(PINS, PWMS)
# Enable the motors at full power going forwards
MOTORS.move(1, 1)

# Open a try statement which allows for clean exit upon Ctrl+C
try:

    # Loop the time sleep so the motors run constantly
    while True:
    	time.sleep(0.1)

# Wait for the Ctrl+C Input then stop all motors and close the script
except KeyboardInterrupt:
        # Stop motors and cleanup the GPIO pins
        MOTORS.stop()
        MOTORS.cleanup()

        # Display Debug Information
        os.system("clear")
        print ("Exiting")

        # Quit program
        exit(0)
