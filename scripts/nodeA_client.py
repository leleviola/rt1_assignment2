#! /usr/bin/env python3
import rospy
import select
#import geometry_msgs.msg
#from nav_msgs.msg import Odometry
import actionlib
import actionlib.msg
import assignment_2_2023.msg
from assignment_2_2023.msg import PosVel
from nav_msgs.msg import Odometry
from assignment_2_2023.srv import GoalPos
#from actionlib_msgs.msg import GoalStatus
import sys

pub = rospy.Publisher('/pos_vel', PosVel, queue_size=10)
#pub2 = rospy.Publisher('/goal_pos', GoalPos, queue_size=10)

def callback(msg):
    vel = PosVel()
    vel.x = msg.pose.pose.position.x
    vel.y = msg.pose.pose.position.y
    vel.vx = msg.twist.twist.linear.x
    vel.vy = msg.twist.twist.linear.y
    pub.publish(vel)
    #customvel = Vel()
    #customvel.name = "linear"
    #customvel.vel = vel.linear.x
    #pub2.publish(customvel)
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

        rospy.loginfo("\n please enter the goal position: ")
        try:
            goal.target_pose.pose.position.x = float(input("x: ")) # define x of the goal
            goal.target_pose.pose.position.y = float(input("y: ")) # define y of the goal
            print(type(goal.target_pose.pose.position.x))
            print(type(goal.target_pose.pose.position.y))
            client.send_goal(goal)
            #pub2.publish(goal.target_pose.pose.position.x, goal.target_pose.pose.position.y)
            # target cancelation
            
            print("press 'c' to cancel the goal: ")
            while(client.get_state() != actionlib.GoalStatus.SUCCEEDED):
                i, o, e = select.select( [sys.stdin], [], [], 1.0 )
                if (i):
                    cancel = sys.stdin.readline().strip()
                    if cancel == 'c':
                        client.cancel_goal()
                        print("goal canceled...")
                        break
            # Sends the goal to the action server.
            if(client.get_state() == actionlib.GoalStatus.SUCCEEDED):
                print("goal has been reached! :)")
            
            
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
        rospy.Subscriber("/odom", Odometry, callback)
        #x = Odometry().pose.pose.position.x
        #y = Odometry().pose.pose.position.y
        #vx = Odometry().twist.twist.linear.x
        #vy = Odometry().twist.twist.linear.y
        #pub.publish(x, y, vx, vy)
        action_client()
        #result = action_client()
        #print("Result:", result)

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)