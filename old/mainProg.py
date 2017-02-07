# Python2 ACK 20/12/2016

# main programme for putting the whole thing together and making it into a real piBot

"""

Setting up the pins:

Back Wheels: 
    A - 9     (Forward drive)
    B - 10    (Backward drive)
    E - 11    (No visible effect, some kind of earthing system?)
    
NB: Pins 23-25, while labelled motor 2 in other programs, don't actually do a thing.

GPIO.setmode(GPIO.BCM)
"""
"""
# Imports for the testing program
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

testMotor =   # Just put the number for the motor you wish to test here

GPIO.setup(testMotor,GPIO.OUT)  # Change to IN if needs be


GPIO.output(testMotor,GPIO.HIGH)  # Provide the pin its current

sleep(5)  # Adjust if you like

GPIO.output(testMotor,GPIO.LOW)  # Take its current away again

GPIO.cleanup()  # Because one must
"""
