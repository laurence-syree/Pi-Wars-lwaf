import RPi.GPIO as GPIO
import time

# pin = 11
# pin2 = 13
# pin3 = 15

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(pin, GPIO.IN)
# GPIO.setup(pin2, GPIO.IN)
# GPIO.setup(pin3, GPIO.IN)
# while True:
# 	print (str(GPIO.input(pin)) + str(GPIO.input(pin2)) + str(GPIO.input(pin3)))

# 	time.sleep(0.2)

def checkSensor(pin):
	GPIO.setup(pin, GPIO.IN)
	return not GPIO.input(pin)
