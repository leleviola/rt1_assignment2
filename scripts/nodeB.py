#! /usr/bin/env python3
import rospy
import assignment_2_2023.msg
import actionlib


def get_last_goal():
    # take the last value of the goal from server
    goal = assignment_2_2023.msg.PlanningGoal()
    x = goal.target_pose.pose.position.x
    y = goal.target_pose.pose.position.y
    return goal

if '__init__' == '__main__':
    try:
        rospy.init_node('nodeA_client')
        [x, y] = get_last_goal()
        print("the last goal is: x= %f, y= %f" %(x, y))
        rospy.spin()
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)