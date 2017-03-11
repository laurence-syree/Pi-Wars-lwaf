import RPi.GPIO as GPIO

def checkSensor(pin):
	GPIO.setup(pin, GPIO.IN)
	return not GPIO.input(pin)
