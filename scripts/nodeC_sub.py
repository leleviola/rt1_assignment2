#! /usr/bin/env python3
import rospy
import assignment_2_2023.msg
import sys
from assignment_2_2023.srv import GoalPos, GoalPosResponse
from assignment_2_2023.srv import DisAvg, DisAvgResponse
from assignment_2_2023.msg import PosVel
import math

x = 0
y = 0
vx = 0
vy = 0
summx = 0
summy = 0
count = 0
def calc_dist_avg(req):
    # this was a my idea, that I didn't implemented because I was not sure it would have respected the scope of the assignment, but I think that it could be a good thing to use node b as a client and node c as the server that elaborates the last goal x and y
    #gx = req.goal_x
    #gy = req.goal_y
    gx=rospy.get_param('des_pos_x')
    gy=rospy.get_param('des_pos_y')
    dist = math.sqrt((gx - x)**2 + (gy - y)**2)
    avg_vx = summx / count
    avg_vy = summy / count
    return DisAvgResponse(dist, avg_vx, avg_vy)
    
    
def retrieve_pos_vel(msg):
    global summx
    global summy
    global count
    x = msg.x
    y = msg.x
    vx = msg.vx
    vy = msg.vy
    summx = summx + vx
    summy = summy + vy
    count = count +1
    
if __name__ == '__main__':
    rospy.init_node('nodeC_sub')
    rospy.Subscriber('/pos_vel', PosVel, retrieve_pos_vel)
    rospy.Service("nodeC", DisAvg, calc_dist_avg)
    rospy.spin()
