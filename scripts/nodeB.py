#! /usr/bin/env python3
import rospy
import assignment_2_2023.msg
import sys
from assignment_2_2023.srv import GoalPos, GoalPosResponse

x = 0
y = 0

        
def callback(req):
    global x
    global y
    x=rospy.get_param('des_pos_x')
    y=rospy.get_param('des_pos_y')
    return GoalPosResponse(x, y)

def take_goal(msg):
    global x, y
    x = msg.target_pose.pose.position.x
    y = msg.target_pose.pose.position.y

if __name__ == '__main__':
    rospy.init_node('nodeB') # init the node
    rospy.Service("nodeB", GoalPos, callback) # initializes the server   
    rospy.spin() # keep the node running
