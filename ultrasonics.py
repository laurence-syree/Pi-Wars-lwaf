  # Python 3 ultrasonics code

  # Trigger is board number 4 (same for all)

  # Echo: board number 7

import RPi.GPIO as GPIO
from time import sleep
from time import time

GPIO.setmode(GPIO.BOARD)

def readSensor(Echo, Trigger):
	while True:
	  GPIO.setup(Triggers,GPIO.OUT)  # Set pin as output device
	  GPIO.output(Triggers, 0)  # Output nothing??

	  sleep(0.1)

	  print"Sending Trigger"
	  # Send pulse, wait a fraction of a second and then stop sending
	  GPIO.output(Triggers,1)  
	  sleep(0.00001)
	  GPIO.output(Triggers,0)
	  
	  GPIO.setup(Echo,GPIO.IN)  # Set pin to input device

	  while GPIO.input(Echo) == 0:  # While pin has no input, do nothing. Waiting for pulse to travel
	    pass
	  start = time()  # Once the loop is broken, start timing

	  while GPIO.input(Echo) == 1:  # Wait for input to stop
	    pass
	  stop = time()  # stop timing
	  # Calculate and output distance between US and object.
	  elapsed = stop - start
	  distance = elapsed * 17000
	  print"Distance %.1f " % distance  # Output the distance travelled (in....?)

	  sleep(2)  # Wait a second, rinse and repeat
 
readSensor(7, 4)
# Reset the GPIO
GPIO.cleanup()