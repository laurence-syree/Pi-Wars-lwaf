""" Library for controlling motors through the pi's GPIO """
# Next line is for the sublime pylinter plugin
# pylint: disable = I0011, C0103, R0201, C0330, C0103
# Import the GPIO library so we can control the GPIO pins
import RPi.GPIO as GPIO


def normspeed(input_data):
    """ Normalises an input range value to the range required by the motors (direcitonally) """
    back = False
    abs_input_data = abs(input_data)
    OldRange = (1 - 0)
    NewRange = (90 - 35)
    NewValue = (((abs_input_data - 0) * NewRange) / OldRange) + 35
    if input_data < 0:
        back = True
    return NewValue, back

# Create a central class called managment
class Management():
    """ Class for motor control mangment (main class) """
    # When an instance of the managment class is created setup the motor mechanism
    def __init__(self, pins, pwmPins):
        # Pull in the pins from the initialisation and store them within the class
        self.pinset = pins
        self.pwnset = pwmPins

        # Set the GPIO output method for the script (currently: pin number based assignment)
        GPIO.setmode(GPIO.BOARD)
        # Set the motor GPIO pins to output
        for cur_pin in self.pinset.items()[1]:
            GPIO.setup(cur_pin, GPIO.OUT)

        # Start PWM for the right side of the robot
        GPIO.setup(pwmPins["r"], GPIO.OUT)
        # Create the pwm object with full speed frequency and duty cycle
        self.pwm1 = GPIO.PWM(pwmPins["r"], 50)
        self.pwm1.start(90)

        # Start PWM for the left side of the robot
        GPIO.setup(pwmPins["l"], GPIO.OUT)
        # Create the pwm object with full speed frequency and duty cycle
        self.pwm2 = GPIO.PWM(pwmPins["l"], 50)
        self.pwm2.start(90)

    def move(self, speedLeft, speedRight):
        """ converts a range of 1 to -1 to motor speeds using normspeed then sets motors """
        # Convert the input range 1 to -1 into 90 to 35 motor controllable range using normspeed
        speedleft = normspeed(speedLeft)
        speedright = normspeed(speedRight)

        # Change the duty cycles on both motors according to what has been requested
        self.pwm1.ChangeDutyCycle(speedleft[0])
        self.pwm2.ChangeDutyCycle(speedright[0])

        # Itterate through each pin in the pinset dictionary
        for cur_key, cur_pin in self.pinset.items():
            # Depending on the key for the pin turn it on, used for turning on the spot or reversing
            if speedleft[1]:
                # If the pin currently in operation is a forwards pin enable
                if cur_key.endswith('f'):
                    GPIO.output(cur_pin, GPIO.HIGH)
            elif not speedleft[1]:
                # If the user has given a reverse command, enable the backwards pins
                if cur_key.endswith('b'):
                    GPIO.output(cur_pin, GPIO.HIGH)

            # Do the same for the right side of the robot
            if speedright[1]:
                if cur_key.endswith('f'):
                    GPIO.output(cur_pin, GPIO.HIGH)
            elif not speedright[1]:
                if cur_key.endswith('b'):
                    GPIO.output(cur_pin, GPIO.HIGH)

    def stop(self):
        """ Set all GPIO pins to low to kill any movement """
        for cur_pin in self.pinset.items()[1]:
            GPIO.output(cur_pin, GPIO.LOW)

    def cleanup(self):
        """ Clears all hold on GPIO pins, called when finished using this object """
        GPIO.cleanup()
