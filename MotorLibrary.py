""" Library for controlling motors through the pi's GPIO """
# Next line is for the sublime pylinter plugin
# pylint: disable = I0011, C0103, R0201, C0330, C0103
# Import the GPIO library so we can control the GPIO pins
import RPi.GPIO as GPIO

SPEED = 0
DIRECTION = 1

def normspeed(input_data):
    return (abs(input_data)*80) + 10, input_data < 0

# Create a central class called managment
class management():
    """ Class for motor control mangment (main class) """
    # When an instance of the managment class is created setup the motor mechanism
    def __init__(self, pins, pwmPins):
        # Pull in the pins from the initialisation and store them within the class
        self.pinset = pins
        self.pwnset = pwmPins

        # Set the GPIO output method for the script (currently: pin number based assignment)
        GPIO.setmode(GPIO.BOARD)
        # Set the motor GPIO pins to output
        for cur_key, cur_pin in self.pinset.items():
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
        self.stop()
        """ converts a range of 1 to -1 to motor speeds using normspeed then sets motors """
        # Convert the input range 1 to -1 into 90 to 35 motor controllable range using normspeed
        normLeft = normspeed(speedLeft)
        normRight = normspeed(speedRight)

        # Change the duty cycles on both motors according to what has been requested
        if normLeft[SPEED] != 0:
            self.pwm1.ChangeDutyCycle(normLeft[SPEED])
        if normRight[SPEED] != 0:
            self.pwm2.ChangeDutyCycle(normRight[SPEED])

        # Itterate through each pin in the pinset dictionary
        for cur_key, cur_pin in self.pinset.items():
            if normLeft[SPEED] != 0:
                if cur_key[1] == 'l':
                    # print "lefting"
                    # Depending on the key for the pin turn it on, used for turning on the spot or reversing
                    if normLeft[DIRECTION]:
                        # If the pin currently in operation is a forwards pin enable
                        if cur_key.endswith('f'):
                            GPIO.output(cur_pin, GPIO.HIGH)
                    elif not normLeft[DIRECTION]:
                        # If the user has given a reverse command, enable the backwards pins
                        if cur_key.endswith('b'):
                            GPIO.output(cur_pin, GPIO.HIGH)

            if normRight[SPEED] != 0:
                if cur_key[1] == 'r':
                    # print "righting"
                    # Do the same for the right side of the robot
                    if normRight[DIRECTION]:
                        if cur_key.endswith('f'):
                            GPIO.output(cur_pin, GPIO.HIGH)
                    elif not normRight[DIRECTION]:
                        if cur_key.endswith('b'):
                            GPIO.output(cur_pin, GPIO.HIGH)
        return normLeft[SPEED], normRight[SPEED]

    def stop(self):
        """ Set all GPIO pins to low to kill any movement """
        for cur_key, cur_pin in self.pinset.items():
            GPIO.output(cur_pin, GPIO.LOW)

    def cleanup(self):
        """ Clears all hold on GPIO pins, called when finished using this object """
        GPIO.cleanup()
