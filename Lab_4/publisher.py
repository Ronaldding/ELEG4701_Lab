# publisher.py
#!/usr/bin/env python  
# -*- coding: utf-8 -*-

# Finish all TODOs.

import sys
import rospy

# TODO 1: import turtlesim/Pose message.
from turtlesim.msg import Pose
# TODO 2: import your Mypose message.
from eleg_t03topic_yoursid.msg import Mypose


def pose_callback(pose):
    rospy.loginfo("Robot 1 X = %f: Y=%f: Z = %f\n", pose.x, pose.y, pose.theta)
    # TODO 3: assign the subscribed pose to your mp.x, mp.y, mp.theta.
    mp.x = pose.x
    mp.y = pose.y
    mp.theta = pose.theta


# Please check with the lecture slides to see how to init a node. You need to do it without TA's help in order to get a full marks for this task.
if __name__ == '__main__':
    # TODO 4: initialize node 'pub_turtle'. 
    rospy.init_node('pub_turtle', anonymous=False)
    # TODO 5: define a publisher: topic name is '/turtle1/Mypose'. 
    pub = rospy.Publisher( '/turtle1/Mypose', Mypose, queue_size=10)  

    # TODO 6: define a subscriber: topic name is '/turtle1/pose'. 
    rospy.Subscriber( '/turtle1/pose', Pose, pose_callback) 

    global mp
    # TODO 7: initialize the variable mp with your message type.  
    mp = Mypose()

    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        # TODO : publish mp.
        pub.publish(mp)
        rate.sleep()

