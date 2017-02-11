import pygame

def clamp(my_value, min_value, max_value):
    return max(min(my_value, max_value), min_value)

pygame.init()
pygame.joystick.init()

controller = pygame.joystick.Joystick(0)
controller.init()

screen = pygame.display.set_mode((100,100))


axis = {}
button = {}

    # these are the identifiers for the PS4's accelerometers
AXIS_X = 3
AXIS_Y = 4

    # variables we'll store the rotations in, initialised to zero
rot_x = 0.0
rot_y = 0.0
triggerDown = False
headingX = 0
trigger = 0

    # main loop
while True:

    for event in pygame.event.get():

        if event.type == pygame.JOYBUTTONDOWN:
                button[event.button] = True
               
                if(event.button == 7):
                        # print(event.button)
                        triggerDown = True

        if event.type == pygame.JOYBUTTONUP:
            if(event.button == 7):
                triggerDown = False

        if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                        headingX = event.value

                if event.axis == 4:
                        
                        scale = (event.value + 1) / 2
                        trigger = scale

    if triggerDown:
        #print(headingX)
        #print(trigger)

        leftValue = trigger - headingX
        rightValue = trigger + headingX

        leftValue = clamp(leftValue, -1, 1)
        rightValue = clamp(rightValue, -1, 1)

        leftValue = round(leftValue, 4)
        rightValue = round(rightValue, 4)

        print(leftValue)
        print(rightValue)





