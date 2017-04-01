This is the code base for our Pi-Wars 2017 entry, Exa-Bot.
All the code is written by us and there is no copy pasted scripts.

Script Reference:

MotorLibrary.py:
This is the script which handles interfacing with the Pi pins in order to control
the direction for each wheel as well as the PWM controlls for both sides of the robot.

controller.py:
This is the script which handles the remote control of the Pi, it connects to a ps4 controller
over bluetooth and watches for events from the remote which controls the functions of the robot

controllerButtonCheck.py:
This script is designed to work out what the ID codes are on the remote in case we need to add
more functionality to the remote. It is modified to print the codes of whatever type of button
you are trying to find the code for.

lineFollower:
This script uses the three lower line folowing modules to follow a line. The robot watches for
different states on the sensors and reacts with the wheels accordingly. The script remembers the
last move it did when it loses the line which usually allows it to correct itself.

maze-test.py:
This script uses the three angled ultrasonic on the front of the robot to navigate a maze with
varying success.

straightline.py:
This script is very simple and is used to make the robot go in a "straight" line by powering the
motors on full with a slight ofset to account for inconstencies in the motors.

ultrasonics.py:
This script is used to check that the ultrasonic sensors are acting as expected. Prints out all
three distance readings from the sensors.
