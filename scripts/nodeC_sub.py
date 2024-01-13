#! /usr/bin/env python3
import rospy
import assignment_2_2023.msg
import sys
from assignment_2_2023.srv import GoalPos, GoalPosResponse
from assignment_2_2023.srv import DisAvg, DisAvgResponse
from assignment_2_2023.msg import PosVel
import math
import subprocess

x = 0
y = 0
vx = 0
vy = 0
#summx = 0
#summy = 0
#count = 0
velx = []
vely =[]
global winsize

def calc_dist_avg(req):
    # this was a my idea, that I didn't implemented because I was not sure it would have respected the scope of the assignment, but I think that it could be a good thing to use node b as a client and node c as the server that elaborates the last goal x and y
    #gx = req.goal_x
    #gy = req.goal_y
    gx=rospy.get_param('des_pos_x')
    gy=rospy.get_param('des_pos_y')
    dist = math.sqrt((gx - x)**2 + (gy - y)**2)
    #avg_vx = summx / count
    #avg_vy = summy / count
    avg_vx = sum(velx)/winsize
    avg_vy = sum(vely)/winsize
    return DisAvgResponse(dist, avg_vx, avg_vy)
    
    
def retrieve_pos_vel(msg):
    global x,y
    global velx, vely
    
    x = msg.x
    y = msg.x
    vx = msg.vx
    vy = msg.vy
    velx.append(vx)
    vely.append(vy)
    if(len(velx)==winsize+1):
        velx = velx[1:] # remove the first element and slide back all the array
    if(len(vely)==winsize+1):
        vely = vely[1:] # remove the first element and slide back all the array
        
    
    
def disp():
    command = "rosservice call /nodeC"
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("distance from target and average x and y speed:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"error executing command: {e}")
        print("command output (stderr):\n", e.stderr)
    
    
if __name__ == '__main__':
    rospy.init_node('nodeC_sub')
    winsize=rospy.get_param('winsize')
    #winsize = 10 ~
    rospy.Subscriber('/pos_vel', PosVel, retrieve_pos_vel)
    rospy.Service("nodeC", DisAvg, calc_dist_avg)
    disp()
    rospy.wait_for_service('nodeC')
    rate = rospy.Rate(2) # frequency in hertz
    #rospy.spin()
    while not rospy.is_shutdown():
    
        disp()
        rate.sleep()
