#!/usr/bin/env python

import rospy
from services_quiz.srv import Move_Robot, Move_RobotResponse
from geometry_msgs.msg import Twist


def move(pub, linear_x=0.0, angular_z=0.0, duration=1.0):

    Cristinei = Twist()
    Cristinei.linear.x = linear_x
    Cristinei.angular.z = angular_z

    rate = rospy.Rate(10)
    start_time = rospy.Time.now().to_sec()
    while rospy.is_shutdown() and (rospy.Time.now().to_sec() - start_time) < duration:
        pub.publish(Cristinei)
        rate.sleep()

def traseu(request):
    move(0.2, 0.0, 2)
    move(0.5, 1.0, 4)
    move(0.2, 0.0, 3.0)
    return Move_RobotResponse(True)


rospy.init_node('move_robot')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
service_srv = rospy.Service('/move_robot', Move_Robot, traseu)
rospy.spin()
