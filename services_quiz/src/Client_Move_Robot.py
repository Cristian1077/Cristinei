#!/usr/bin/env python

import rospy
from services_quiz.srv import Move_Robot

rospy.init_node('service_move_robot')
rospy.wait_for_service('/move_robot')
service = rospy.ServiceProxy('/move_robot', Move_Robot)
direction = input('direction (forward/left): ')
duration = float(input('duration: '))

result = service(direction, duration)

print(result.success)
print(result.message)
