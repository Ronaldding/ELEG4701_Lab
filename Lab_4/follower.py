# follower.py
#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import sys
import rospy
# TODO 1: import math to use atan2() easily.
import math
# TODO 2: import all message types you need.
from geometry_msgs.msg import Twist
from eleg_t03topic_yoursid.msg import Mypose
from turtlesim.msg import Pose

def pose_callback(pose):
    global ROBOT_X
    global ROBOT_Y
    global ROBOT_T

    rospy.loginfo("Robot 2 X = %f: Y=%f: Z = %f\n", pose.x, pose.y, pose.theta)
    # TODO 3: assign the robot pose to the global variables.
    ROBOT_X = pose.x
    ROBOT_Y = pose.y
    ROBOT_T = pose.theta


def myPose_callback(myPose):
    # TODO 4: The speed is controlled by the difference between the poses of the two robots to achieve following. 
    # Hints:   1. P-control: Use k times the position difference between the X and Y axis to control the x linear speed. 
    #          2. Make the angle of the robot2 always face the other robot. 
    #          3. Think about how to calculate the difference of two angles using atan2()

    # P-Control
    x_diff = myPose.x - ROBOT_X
    y_diff = myPose.y - ROBOT_Y
    t_diff = math.atan2(y_diff, x_diff) - ROBOT_T

    if t_diff > math.pi:
        t_diff = t_diff - 2 * math.pi
    elif t_diff < -math.pi:
        t_diff = t_diff + 2 * math.pi

    linear_diff = math.sqrt(math.pow(x_diff, 2)+ math.pow(y_diff, 2))

    k = 0.2

    vel.linear.x = 0.2 * abs(x_diff)
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 5 * t_diff


if __name__ == '__main__':
    # TODO 5: initialize node 'follow_turtle'
    rospy.init_node('follow_turtle', anonymous=False)
    # TODO 6: define a publisher: topic name is '/turtle2/cmd_vel'. 
    pub = rospy.Publisher( '/turtle2/cmd_vel', Twist, queue_size=10) 
    # TODO 7: define a subscriber: topic name is '/turtle1/Mypose'. 
    rospy.Subscriber( '/turtle1/Mypose', Mypose, myPose_callback)  
    # TODO 8: define a subscriber: topic name is '/turtle2/pose'. 
    rospy.Subscriber( '/turtle2/pose', Pose, pose_callback)  

    global vel
    # TODO 9: initialize the variable vel with the message type.  
    vel = Twist()

    rate = rospy.Rate(10)       
    while not rospy.is_shutdown():
        # TODO : publish vel.
        pub.publish(vel)

        rate.sleep()



