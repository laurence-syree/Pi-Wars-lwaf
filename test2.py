import RPi.GPIO as GPIO
from time import sleep
from time import time
import os
import sys

Motor1A = 11
Motor1B = 9

Echo = 26  # The ultrasound is pin 26

GPIO.setmode(GPIO.BCM)



while True:
  GPIO.setmode(GPIO.BCM)

  GPIO.setup(Echo,GPIO.OUT)  # Set pin as output device
  GPIO.setup(Motor1A,GPIO.OUT)
  GPIO.setup(Motor1B,GPIO.OUT)

  GPIO.output(Echo, 0)  # Output nothing??

  sleep(0.1)

  print "Sending Trigger"
  # Send pulse, wait a fraction of a second and then stop sending
  GPIO.output(Echo,1)  
  sleep(0.00001)
  GPIO.output(Echo,0)
  
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
  print "Distance %.1f " % distance  # Output the distance travelled (in....?)
 
  if distance < 2.8:  
	break


  sleep(1)  # Wait a second, rinse and repeat
  print "Turning motor on"
  GPIO.output(Motor1A,GPIO.HIGH)
  GPIO.output(Motor1B,GPIO.HIGH)  
 
  if distance > 60:
  	sleep(0.5)
  elif distance > 7 :
	sleep(0.1)
  else:
	sleep(0.01)
  



  print "Stopping motor"
  GPIO.output(Motor1A,GPIO.LOW)
  GPIO.output(Motor1B,GPIO.LOW)
  GPIO.cleanup()
	

# tempVal = "50%"
# os.system("echo 0=%s > /dev/servoblaster"%tempVal)

# echo 0=50% > /dev/servoblaster
# echo 0=-20 > /dev/servoblaster
# echo 0=+20 > /dev/servoblaster






