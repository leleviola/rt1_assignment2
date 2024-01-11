#! /usr/bin/env python3
import rospy
#import geometry_msgs.msg
#from nav_msgs.msg import Odometry
import actionlib
import actionlib.msg
import assignment_2_2023.msg
from assignment_2_2023.msg import PosVel
from nav_msgs.msg import Odometry
#from actionlib_msgs.msg import GoalStatus
import sys

pub = rospy.Publisher('/pos_vel', PosVel, queue_size=10)

def action_client(): #function to set the goal
    # Creates the SimpleActionClient, passing the type of the action
    client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2023.msg.PlanningAction)
    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()
    # Creates a goal to send to the action server.
    goal = assignment_2_2023.msg.PlanningGoal()
    # Define the goal
    #goal.target_pose.header.frame_id = "goal" # define the frame
    while not rospy.is_shutdown(): # while ros is running
        #pub = PosVel()
        

        rospy.loginfo("\n Please enter the goal position: ")
        try:
            goal.target_pose.pose.position.x = float(input("x: ")) # define x of the goal
            goal.target_pose.pose.position.y = float(input("y: ")) # define y of the goal
            print(type(goal.target_pose.pose.position.x))
            print(type(goal.target_pose.pose.position.y))
            client.send_goal(goal)
            # target cancelation
            cancel = input("Press 'c' to cancel the goal: ")
            if cancel == 'c':
                client.cancel_goal()
            else:
                print("The goal is still active.")
            # Sends the goal to the action server.
            
        except ValueError:
            print("Invalid input, please enter a number.")
        
    
    # Waits for the server to finish performing the action.
    #client.wait_for_result()
    # Prints out the result of executing the action
    #return client.get_result()
    
if __name__ == '__main__': # entry point of Python script. 
    # It tells Python to run the code below only if the module is executed as the main program.
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('nodeA_client')
        x = Odometry().pose.pose.position.x
        y = Odometry().pose.pose.position.y
        vx = Odometry().twist.twist.linear.x
        vy = Odometry().twist.twist.linear.y
        pub.publish(x, y, vx, vy)
        action_client()
        #result = action_client()
        #print("Result:", result)

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)