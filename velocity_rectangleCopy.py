#!/usr/bin/env python
# -*- coding: utf-8 -*-
#this example will pub turtle1/cmd_vel topic，message type is geometry_msgs::Twist, node name is velocity_publisher_last 3 number of you SID,
#example: sid 1155135432 and the node name will be velocity_publisher_432

# Todo 0: modify the package.xml file, add rospy dependence; set eniveriment in ./bashrc file so that you do not need to source every time，
# visit this site https://answers.ros.org/question/211008/where-is-my-bashrc-file-in-ros/ to get some help. add this command to the file "source ~/catkin_ws/devel/setup.bash"

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute


def velocity_publisher():

    rospy.init_node('rectangle_drawer', anonymous=True)
    turtle_teleport_pub = rospy.Publisher('turtle1/teleport_absolute', TeleportAbsolute, queue_size=10)
    rate = rospy.Rate(1)

    teleport_msg = TeleportAbsolute()
    teleport_msg.x = 1
    teleport_msg.y = 1
    teleport_msg.theta = 0
    turtle_teleport_pub.publish(teleport_msg)

    width = 3
    height = 4

    teleport_msg.x += width
    turtle_teleport_pub.publish(teleport_msg)
    rate.sleep()

    teleport_msg.y += height
    turtle_teleport_pub.publish(teleport_msg)
    rate.sleep()

    teleport_msg.x -= width
    turtle_teleport_pub.publish(teleport_msg)
    rate.sleep()

    teleport_msg.y -= height
    turtle_teleport_pub.publish(teleport_msg)
    rate.sleep()
    #  rospy.init_node('velocity_publisher_520', anonymous=True)
    #  turtle_vel_pub = rospy.Publisher('turtle1/teleport_absolute', TeleportAbsolute, queue_size=10)
    #  rate = rospy.Rate(1000)
    #  while not rospy.is_shutdown():
    #      vel_msg = TeleportAbsolute()
    #      vel_msg.linear.x = 10
    #      vel_msg.linear.y = 0
    #      vel_msg.linear.z = 0
    #      vel_msg.angular.x = 0
    #      vel_msg.angular.y = 0
    #      vel_msg.angular.z = 0
    #      turtle_vel_pub.publish(vel_msg)
    #      rospy.loginfo("Publish turtle velocity command: linear=%.3f, angular=%.3f", vel_msg.linear.x, vel_msg.angular.z)
    #      rate.sleep()


    # # Todo 1, ROS node initialize
	# # create a Publisher, queue size is 10
    # # Todo 2: finish the code below 
    # # reference: rospy.Publisher(topic_name, msg_class, queue_size)
    # #turtle_vel_pub = rospy.Publisher(topic_name='turtle1/cmd_vel', msg_class=Twist, queue_size=10)
    # # turtle_vel_pub = rospy.Publisher( topic_name, msg_class, queue_size=10)
	# #set loop rate
    # rate = rospy.Rate(10) 
    # while not rospy.is_shutdown():
	# 	# init geometry_msgs::Twist
    #     vel_msg = Twist()
    #     # Todo 3: draw a circle, the linear velocity is π m/s, and radius is π m
    #     # modify the code below and import something at the start of the file, you should use the π in math library rather than 3.14
    #     vel_msg.linear.x = 5
    #     vel_msg.linear.y = 0
    #     vel_msg.linear.z = 0
    #     vel_msg.angular.x = 0
    #     vel_msg.angular.y = 0
    #     vel_msg.angular.z = 10
	# 	# publish
    #     turtle_vel_pub.publish(vel_msg)
    #     # turtle_vel_pub.publish(vel_msg)
    #     #Todo 4: modify the code below, let the terminal output 2 velocities,hold 3 digits after the decimal point
    # 	rospy.loginfo("Publish turtle velocity command: linear=%.3f, angular=%.3f", vel_msg.linear.x, vel_msg.angular.z)
	# 	# delay as loop rate
    #     rate.sleep()

if __name__ == '__main__':
    try:    
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass