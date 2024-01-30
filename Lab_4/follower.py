#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import sys
import rospy
# TODO 1: import math to use atan2() easily.
# TODO 2: import all message types you need.

def pose_callback(pose):
    global ROBOT_X
    global ROBOT_Y
    global ROBOT_T

    rospy.loginfo("Robot 2 X = %f: Y=%f: Z = %f\n", pose.x, pose.y, pose.theta)
    # TODO 3: assign the robot pose to the global variables.


def myPose_callback(myPose):
    # TODO 4: The speed is controlled by the difference between the poses of the two robots to achieve following. 
    # Hints:   1. P-control: Use k times the position difference between the X and Y axis to control the x linear speed. 
    #          2. Make the angle of the robot2 always face the other robot. 
    #          3. Think about how to calculate the difference of two angles using atan2()


if __name__ == '__main__':
    # TODO 5: initialize node 'follow_turtle'
    # TODO 6: define a publisher: topic name is '/turtle2/cmd_vel'. 
    # TODO 7: define a subscriber: topic name is '/turtle1/Mypose'. 
    # TODO 8: define a subscriber: topic name is '/turtle2/pose'. 

    global vel
    # TODO 9: initialize the variable vel with the message type.  
    rate = rospy.Rate(10)       
    while not rospy.is_shutdown():
        # TODO : publish vel.

        rate.sleep()



