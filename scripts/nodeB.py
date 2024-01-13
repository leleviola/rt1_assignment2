#! /usr/bin/env python3
import rospy
import assignment_2_2023.msg
import sys
from assignment_2_2023.srv import GoalPos, GoalPosResponse

x = 0
y = 0
def send_goal_position_request(x, y):
    rospy.wait_for_service('nodeC_service')  # Replace with the actual service name in nodeC

    try:
        # Create a service proxy
        service_proxy = rospy.ServiceProxy('nodeC_service', DisAvg)

        # Make the service request
        response = service_proxy(x, y)

        # Process the response (if needed)
        process_response(response)

    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        
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
