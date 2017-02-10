import RPi.GPIO as GPIO
from time import sleep

direction = "l"
distance = 4

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

GPIO.setmode(GPIO.BOARD)
# Setup the GPIO pins ready for control
for key, pin in pins.items():
	GPIO.setup(pin,GPIO.OUT)

# Based on direction set the required direction pin to high
if direction == "f":
	# GPIO.setup(22, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port they need  
	# p = GPIO.PWM(22, 50)    # create an object p for PWM on port 25 at 50 Hertz  
	#                         # you can have more than one of these, bu
	#                         # different names for each port   
	#                         # e.g. p1, p2, motor, servo1 etc.  
	  
	# p.start(90)             # start the PWM on 50 percent duty cycle  
	#                         # duty cycle value can be 0.0 to 100.0%, floats are OK 

	for key, pin in pins.items():
		if key.endswith('f'):
			GPIO.output(pin, GPIO.HIGH)

elif direction == "b":
	for key, pin in pins.items():
		if key.endswith('b'):
			GPIO.output(pin, GPIO.HIGH)
			print ("hello")

elif direction == "l":
	for key, pin in pins.items():
		if key[1] == 'l' and key.endswith('b'):
			GPIO.output(pin, GPIO.HIGH)
		if key[1] == 'r' and key.endswith('f'):
			GPIO.output(pin, GPIO.HIGH)
else:
	# If invalid direction throw error
	raise ValueError("Invalid direction specified", direction)

try:
	sleep(float(distance))
except:
	# Set all GPIO pins to low to kill any movement
	for key, pin in pins.items():
		GPIO.output(pins, GPIO.LOW)

	# If invalid distance throw error
	raise ValueError("Invalid Distance Specified", distance)
	# Release hold on GPIO pins
	GPIO.cleanup()

# Set all GPIO pins to low to kill any movement
for key, pin in pins.items():
	GPIO.output(pin, GPIO.LOW)

#p.stop()
# Release hold on GPIO pins
GPIO.cleanup()