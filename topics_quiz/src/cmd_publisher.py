#! /usr/bin/env python

import rospy                                          
from geometry_msgs.msg import Twist

rospy.init_node('bot_movement')
sub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.sleep(1.0)

def trimite(v_lin, v_ang, timp):
	msg = Twist()
	msg.linear.x, msg.angular.z = v_lin, v_ang
	pub.publish(msg)
	time.sleep(timp)


