#! /usr/bin/env python3
import rospy
import assignment_2_2023.msg
import sys
from assignment_2_2023.srv import GoalPos, GoalPosResponse

def callback(req):
    return GoalPosResponse(req.x, req.y)

def take_goal(msg):
    global x 
    global y
    x = msg.target_pose.pose.position.x
    y = msg.target_pose.pose.position.y
    print("x: ")
    print(x)
    print("y: ")
    print(y)

if '__init__' == '__main__':
    rospy.init_node('nodeB') # init the node
    #rospy.Service('/goal_pos', GoalPos, callback)
    rospy.Service("nodeB", GoalPos, callback)
    #[x, y] = get_last_goal() # take the last goal
    rospy.Subscriber("/reaching_goal/goal", assignment_2_2023.msg.PlanningGoal, take_goal)
    rospy.spin() # keep the node running