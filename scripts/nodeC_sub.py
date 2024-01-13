#! /usr/bin/env python3
import rospy
import assignment_2_2023.msg
import sys
from assignment_2_2023.srv import GoalPos, GoalPosResponse
from addignment_2_2023.srv import DisAvg, DisAvgResponse
from assignment_2_2023.msg import PosVel
import math

x = 0
y = 0
vx = 0
vy = 0

def calc_dist_avg(req)
    gx = req.x
    gy = req.y
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(gx)
    print(gy)
    
def retrieve_pos_vel(msg):
    x = msg.x
    y = msg.x
    vx = msg.vx
    vy = msg.vy
    
if __name__ == '__main__':
    rospy.init_node('nodeC_sub')
    rospy.Service("nodeC", DisAvg, calc_dist_avg)
    
    rospy.Subscriber('/pos_vel', PosVel, retrieve_pos_vel)
    rospy.spin()
