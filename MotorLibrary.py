import RPi.GPIO as GPIO

class management ():
	def __init__ (self, pins, pwmPins):
		self.pinset = pins
		self.pwnset = pwmPins

		GPIO.setmode(GPIO.BOARD)
		# Setup the GPIO pins ready for control
		for cur_key, cur_pin in self.pinset.items():
			GPIO.setup(cur_pin,GPIO.OUT)

		# Start PWM for the right side of the robot
		GPIO.setup(pwmPins["r"], GPIO.OUT)
		self.pwm1 = GPIO.PWM(pwmPins["r"], 50)
		self.pwm1.start(90)

		# Start PWM for the left side of the robot
		GPIO.setup(pwmPins["l"], GPIO.OUT)
		self.pwm2 = GPIO.PWM(pwmPins["l"], 50)
		self.pwm2.start(90)

	def normspeed(self, input_data):
		back = False
		abs_input_data = abs(input_data)
		OldRange = (1 - 0)  
		NewRange = (90 - 35)  
		NewValue = (((abs_input_data - 0) * NewRange) / OldRange) + 35
		if input_data < 0:
			back = True
		return NewValue, back

	def move (self, speedLeft, speedRight):
		speedleft = self.normspeed(speedLeft)
		speedright = self.normspeed(speedRight)

		self.pwm1.ChangeDutyCycle(speedleft[0])
		self.pwm2.ChangeDutyCycle(speedright[0])

		for cur_key, cur_pin in self.pinset.items():

				if speedleft[1]:
					if cur_key.endswith('f'):
						GPIO.output(cur_pin, GPIO.HIGH)
				elif not(speedleft[1]):
					if cur_key.endswith('b'):
						GPIO.output(cur_pin, GPIO.HIGH)

				if speedright[1]:
					if cur_key.endswith('f'):
						GPIO.output(cur_pin, GPIO.HIGH)
				elif not(speedright[1]):
					if cur_key.endswith('b'):
						GPIO.output(cur_pin, GPIO.HIGH)

	def stop(self):
		# Set all GPIO pins to low to kill any movement
		for cur_key, cur_pin in self.pinset.items():
			GPIO.output(cur_pin, GPIO.LOW)

	def cleanup (self):

		# Release hold on GPIO pins
		GPIO.cleanup()