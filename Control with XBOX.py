"""
How to take the really cool parts of the Anki Vector and make it not do those.
Control vector with a controller.

James Anderson - December 2018

All comments on corresponding control comments are to XBox Controllers.
"""

from inputs import get_gamepad
import inputs
from math import inf
import random
import anki_vector
from time import sleep

with anki_vector.AsyncRobot() as robot:
    l_mod = 1
    r_mod = 1
    right = 0
    left = 0
    head = 0
    arm = 0
    while 1:
        events = get_gamepad()
        for event in events:
            #Left Bumper
            if event.code == "BTN_TL":
                #Pressed
                if event.state == 1:
                    l_mod = -1
                #Relesead
                else:
                    l_mod = 1
            #Right Bumper
            if event.code == "BTN_TR":
                #Pressed
                if event.state == 1:
                    r_mod = -1
                #Released
                else:
                    r_mod = 1
            #Right Trigger
            if event.code == "ABS_RZ":
                right = event.state
            #Left Trigger
            if event.code == "ABS_Z":
                left = event.state
            #A Button
            if event.code == "BTN_SOUTH":
                #Pressed
                if event.state == 1:
                    robot.say_text("bbt. bbt. bbtbbt")
            #B Button
            if event.code == "BTN_EAST":
                #Pressed
                if event.state == 1:
                    for x in range (5):
                        robot.say_text("VECTOR is the best! bow in his presence.")
            #X Button
            if event.code == "BTN_WEST":
                #Pressed
                if event.state == 1:
                    robot.say_text("Michael has good ideas but they are hard to program")
            #DPad Up/DOWN
            if event.code == "ABS_HAT0Y":
                #UP
                if event.state == -1:
                    robot.motors.set_lift_motor(100)
                #Down
                if event.state == 1:
                    robot.motors.set_lift_motor(-100)
            #DPad Left/Right
            if event.code == "ABS_HAT0X":
                #Left
                if event.state == -1:
                    robot.motors.set_head_motor(-10)
                #Right
                if event.state == 1:
                    robot.motors.set_head_motor(10)
            print(event.ev_type, event.code, event.state)
            robot.motors.set_wheel_motors(left*l_mod,right*r_mod,inf,inf)