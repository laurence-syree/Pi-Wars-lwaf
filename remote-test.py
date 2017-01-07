# import time
import os
import sys

# tempVal = "50%"
# os.system("echo 0=%s > /dev/servoblaster"%tempVal)

# echo 0=50% > /dev/servoblaster
# echo 0=-20 > /dev/servoblaster
# echo 0=+20 > /dev/servoblaster


import RPi.GPIO as GPIO
from time import sleep

direction = raw_input("For forwards put 'f' for backwards put 'b' : ") 
time = raw_input("How long would you like the robot to run for /seconds : ")


GPIO.setmode(GPIO.BCM)

Motor1A = 9  # 
Motor1B = 10  # black
Motor1E = 11
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
print "Turning motor on"

if direction == "f":

	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
else:
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(float(time))
 
print "Stopping motor"
GPIO.output(Motor1A,GPIO.LOW)
 
GPIO.cleanup()
