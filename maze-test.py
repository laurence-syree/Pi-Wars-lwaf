import RPi.GPIO as GPIO
import time
import motorLibrary

GPIO.setmode(GPIO.BOARD)

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
MOTORS.stop()



def readSensor(Echo, Trigger):
	GPIO.setup(Trigger,GPIO.OUT)  # Set pin as output device
	GPIO.output(Trigger, 0)  # Output nothing??

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
	distance = round(distance, 0)
	return distance

left = 20
forwards = 40
right = 20

mem1 = False
mem2 = False
mem3 = False


while True:
	left = readSensor(3, 8)
	forwards = readSensor(5, 8)
	right = readSensor(7, 8)
	

	if forwards > 30 and left > 20 and right > 20:
		dire = "f"

	elif left > right:  
		dire = "l"

	else:
		dire = "r"
		
	if dire != "f" and int(left/10) == int(right/10):
		print ("Stuckk")
		if mem3:
			dire = "l"
		else:
			dire = "r"


	if dire == "f":
		MOTORS.move(0.4, 0.4)
		time.sleep(0.25)
		MOTORS.stop()


	elif dire == "l":  
		#print ("turn Left")
		MOTORS.move(1, -1)
		time.sleep(0.25)
		MOTORS.stop()

	else:
		# Right
		MOTORS.move(-1, 1)
		time.sleep(0.25)
		MOTORS.stop()

	mem2, mem3 = mem1, mem2
	if left > right:
		mem1 = True
	else:
		mem1 = False

	print ("dire:" + dire + " left: " + str(left) + " forwards: " + str(forwards) + " Right: " + str(right) + " 1: " + str(mem1) + " 2: " + str(mem2) + " 3: " + str(mem3))
