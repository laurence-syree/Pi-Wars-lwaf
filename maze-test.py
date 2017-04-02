# Import built in libraries
import RPi.GPIO as GPIO
import time
# Import the motor library for motor control
import MotorLibrary

# Set the GPIO numbering type to BOARD
GPIO.setmode(GPIO.BOARD)

# Pin set for controlling the motors direction
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

# Pin set for controlling the motor speed
PWMS = {
	"l" : 16,
	"r" : 18
}

# Create an instance of the motor library and stop the motors
MOTORS = MotorLibrary.management(PINS, PWMS)
MOTORS.stop()


# Function for reading input from the ultrasonic sensors
def readSensor(Echo, Trigger):
	GPIO.setup(Trigger,GPIO.OUT)  # Set pin as output device
	GPIO.output(Trigger, 0)  # Set the trigger to low (prevents issues on start)

	time.sleep(0.001)

	# Send pulse, wait a fraction of a second and then stop sending
	GPIO.output(Trigger,1)  
	time.sleep(0.0001)
	GPIO.output(Trigger,0)

	GPIO.setup(Echo,GPIO.IN)  # Set pin to input device

	while GPIO.input(Echo) == 0:  # While pin has no input, do nothing. Waiting for pulse to travel
		pass
	start = time.time()  # Once the loop is broken, start timing

	while GPIO.input(Echo) == 1:  # Wait for input to stop
		pass
	stop = time.time()  # stop timing
	# Calculate and output distance between US and object.
	elapsed = stop - start
	distance = elapsed * 17000
	# Round the distance
	distance = round(distance, 0)
	return distance

# Setting the inital values for the system so it goes forwards by default
left = 20
forwards = 40
right = 20

# Memory variables so it knows what to do when it comes into a corner (ish)
mem1 = False
mem2 = False
mem3 = False

# Main Script Loop
while True:
	# Read sensor input
	left = readSensor(3, 8)
	forwards = readSensor(5, 8)
	right = readSensor(7, 8)
	
	# If statement for each movement outcome
	if forwards > 30 and left > 20 and right > 20:
		dire = "f"

	elif left > right:  
		dire = "l"

	else:
		dire = "r"
	
	# Script decides when the robot is stuck and calls upon the memory and overwrites the sensor preference
	# if dire != "f" and int(left/10) == int(right/10):
	if dire != "f" and abs(left-right) <= 8 and left < 15:
		print ("Stuckk")
		if mem3:
			dire = "l"
		else:
			dire = "r"

	# Pulls the data from above and actions the movement
	if dire == "f":
		# Forwards
		MOTORS.move(0.4, 0.4)
		time.sleep(0.25)
		MOTORS.stop()

	elif dire == "l":  
		# Left
		MOTORS.move(1, -1)
		time.sleep(0.15)
		MOTORS.stop()

	else:
		# Right
		MOTORS.move(-1, 1)
		time.sleep(0.15)
		MOTORS.stop()

	# Shuffle the mory over by one
	mem2, mem3 = mem1, mem2
	# Set the top memory value to true if the left sensor is longer than the right sensor
	if left > right:
		# Memory values are true when the robot should turn left to recover (and vise versa)
		mem1 = True
	else:
		mem1 = False

	# Debug output
	print ("dire:" + dire + " left: " + str(left) + " forwards: " + str(forwards) + " Right: " + str(right) + " 1: " + str(mem1) + " 2: " + str(mem2) + " 3: " + str(mem3))
