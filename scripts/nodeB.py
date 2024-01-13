#! /usr/bin/env python3
import rospy
import assignment_2_2023.msg
import sys
from assignment_2_2023.srv import GoalPos, GoalPosResponse

# initializes the coordinates
x = 0
y = 0

def callback(req):
    global x
    global y
    x=rospy.get_param('des_pos_x')
    y=rospy.get_param('des_pos_y')
    return GoalPosResponse(x, y) # sets the response of the service to the last goal coord

if __name__ == '__main__':
    rospy.init_node('nodeB') # init the node
    rospy.Service("nodeB", GoalPos, callback) # initializes the server   
    rospy.spin() # keep the node running
