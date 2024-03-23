#! /usr/bin/env python3

"""
.. module:: nodeA_client

  :platform: Unix
  :synopsis: Python module for the second assignment of research track

.. moduleauthor:: Samuele Viola 

This node's aim is to set, by using keyword, the next goal's position. The goal can be canceled by pressing c key.

Subscriber:
/odom
Publisher:
/pos_vel



"""
import rospy
import select
import actionlib
import actionlib.msg
import assignment_2_2023.msg
from assignment_2_2023.msg import PosVel
from nav_msgs.msg import Odometry
from assignment_2_2023.srv import GoalPos
import sys

pub = rospy.Publisher('/pos_vel', PosVel, queue_size=10)

def callback(msg):
    """

    This function, when called, publish to /pos_vel the robot position and linear and angular velocity

    Args:
        msg: message from /odom

    """
    vel = PosVel()
    vel.x = msg.pose.pose.position.x
    vel.y = msg.pose.pose.position.y
    vel.vx = msg.twist.twist.linear.x
    vel.vz = msg.twist.twist.angular.z
    pub.publish(vel)
    
def action_client(): #function to set the goal
    # Creates the SimpleActionClient, passing the type of the action
    client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2023.msg.PlanningAction)
    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()
    # Creates a goal to send to the action server.
    goal = assignment_2_2023.msg.PlanningGoal()
    
    while not rospy.is_shutdown(): # while ros is running

        rospy.loginfo("\n please enter the goal position: ")
        try:
            goal.target_pose.pose.position.x = float(input("x: ")) # define x of the goal
            goal.target_pose.pose.position.y = float(input("y: ")) # define y of the goal
            client.send_goal(goal)
            # target cancelation
            print("press 'c' to cancel the goal: ")
            while(client.get_state() != actionlib.GoalStatus.SUCCEEDED): # ig the goal has reached we can't cancel the goal
                i, o, e = select.select( [sys.stdin], [], [], 1.0 ) # to set a timeout for the input reading, to check periodically if the goal is reached
                if (i):
                    cancel = sys.stdin.readline().strip()
                    if cancel == 'c':
                        client.cancel_goal() # cancel the goal
                        print("goal canceled...")
                        break
            # Sends the goal to the action server.
            if(client.get_state() == actionlib.GoalStatus.SUCCEEDED):
                print("goal has been reached! :)")
        except ValueError:
            print("invalid input, please enter a number.")
        
    
if __name__ == '__main__': # entry point of Python script. 
    # It tells Python to run the code below only if the module is executed as the main program.
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('nodeA_client')
        rospy.Subscriber("/odom", Odometry, callback) # subscriber to /odom, for reading x,y,vx and vy of the robot
        
        action_client()
        

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
