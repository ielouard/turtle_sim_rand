#!/usr/bin/env python
# coding=utf-8

'''
    File name: limit_service_node.py
    Author: Ibrahim elouard
    Date created: 16/10/2018
    Date last modified: 16/10/2018
    Python Version: 2.7
'''

import rospy, time
from turtlesim.msg import Pose
from std_msgs.msg import String
from turtle_sim_rand.srv import Collision

class Turtle():
    '''
        TODO
    '''
    collision=False
    bord_min=0.6
    bord_max=10.2
    def __init__(self):
        '''
            Fonction d'initialisation du noeud
        '''
        rospy.init_node('limit_service_node')
        rospy.Subscriber("/turtlesim1/turtle1/pose", Pose, self.pose_callback)
        rospy.Service('detect_collision', Collision, self.collision_handle)
        rospy.spin()

    def collision_handle(self,collision_detected):
        '''
            Fonction appelée par le service "collision_detected"
        '''
        if self.collision:
            rospy.loginfo("collision detected")
            #clear screen
            time.sleep(1)
            print("\033c")
            #end of clear screen
        return self.collision

    def pose_callback(self,pose):
        '''
            Fonction de callback du subscriber au topic /turtlesim1/turtle1/pose
            Cette fonction verifie si la tortue est pres d'un bord et modifie la valeur
            du bool collision en fonction
        '''
        if pose.x<self.bord_min or pose.y<self.bord_min or pose.x>self.bord_max or pose.y>self.bord_max:
            rospy.loginfo("x: %s  | Y: %s" , pose.x, pose.y)
            self.collision=True
        else:
            self.collision=False


if __name__ == "__main__":
    tr=Turtle()
