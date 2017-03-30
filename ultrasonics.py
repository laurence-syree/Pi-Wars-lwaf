  # Python 3 ultrasonics code

  # Trigger is board number 4 (same for all)

  # Echo: board number 7

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

def readSensor(Echo, Trigger):
	GPIO.setup(Trigger,GPIO.OUT)  # Set pin as output device
	GPIO.output(Trigger, 0)  # Set the trigger to low (prevents issues on start)

	time.sleep(0.1)

	print"Sending Trigger"
	# Send pulse, wait a fraction of a second and then stop sending
	GPIO.output(Trigger,1)  
	time.sleep(0.00001)
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
	distance = round(distance, 2)
	print "got distance"
	return distance
 
print (readSensor(7, 8))
print (readSensor(5, 8))
print (readSensor(3, 8))
time.sleep(1)
# Reset the GPIO
GPIO.cleanup()