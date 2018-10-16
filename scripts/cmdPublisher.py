#!/usr/bin/env python

# coding=utf-8

import rospy,random
from geometry_msgs.msg import Twist
from turtle_sim_rand.srv import Collision


if __name__ == "__main__":
    vel_msg=Twist()
    rospy.init_node('cmdPublisher')
    call_collision_srv= rospy.ServiceProxy('detect_collision', Collision)
    velocity_publisher = rospy.Publisher('/turtlesim1/turtle1/cmd_vel', Twist, queue_size=10)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        collision= call_collision_srv().collision
        vel_msg.linear.x=2
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = -2 if collision else random.uniform(-5,5)
        velocity_publisher.publish(vel_msg)
        rate.sleep()
