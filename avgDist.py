import RPi.GPIO as GPIO
from time import sleep
from time import time

GPIO.setmode(GPIO.BCM)

Echo = 26  # The ultrasound is pin 26
distArray = []
for i in range(100):
  GPIO.setup(Echo,GPIO.OUT)  # Set pin as output device
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
  distArray.append(distance)
  #sleep(1)  # Wait a second, rinse and repeat

total = 0
for dist in distArray:
  total += dist
total = total/100
print "average distance is " + dist
# Reset the GPIO
GPIO.cleanup()
