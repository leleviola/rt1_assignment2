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
    return GoalPosResponse(x, y)

def take_goal(msg):
    global x 
    global y
    x = msg.target_pose.pose.position.x
    y = msg.target_pose.pose.position.y

if __name__ == '__main__':
    rospy.init_node('nodeB') # init the node
    #rospy.Service('/goal_pos', GoalPos, callback)
    rospy.Service("nodeB", GoalPos, callback)
    #[x, y] = get_last_goal() # take the last goal
    rospy.Subscriber("/reaching_goal", assignment_2_2023.msg.PlanningGoal, take_goal)
    rospy.spin() # keep the node running
