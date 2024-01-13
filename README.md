# Assignment 2: "3D Mobile Robot"

by leleviola

## Introduction
In this project there is a 3D simulator, in which there is mobile robot that moves in a plane, and an environment, a world, with edges and obstacles (walls); you can see  it in the picture below. The original package can bee seen here: https://github.com/CarmineD8/assignment_2_2023.

Other than it, I implemented other three nodes, that will be described in the next section:
- node A
- node B
- node C

During the simulation, there will be opened 5 windows, 2 are needed for the simulation, another one is the one from which you run the program, where there will be displayed som debug messagges, the other 2 are the nodeA and the nodeC
<img src="https://github.com/leleviola/rt1_assignment2/blob/resources/images/Schermata%20del%202024-01-13%2017-20-48.png" alt="Alt Text" width="400"/>



# Nodes description

## Node A: Action Client
This node implements an action client that permits the user to set the target that the robot has to reach. In particular, by the keyboard input the user will send to the action server the new goal coordinates by the topic '/reaching_goal'. The node contains also a subscriber to /Odom, in which you can find the robot's position and velocity in real time, and then publish them to the topic '/pos_vel' using the custom message PosVel. Here there is the pseudocode of this first node.

<img src="https://github.com/leleviola/rt1_assignment2/blob/resources/images/Schermata%20del%202024-01-13%2018-39-31.png" alt="Alt Text" width="1000"/>

## Node B: Last Goal
Node B is a service node, which means that it implements a request/reply communication. The service used in nodeB is GoalPos (GoalPos.srv in srv folder), that is composed only by the response, this is because there isn't any client that makes a request, but it returns, when the service is called, the last goal coordinates. This node in particular hasn't a graphical interface, so it isn't runned in a Xterm terminal. For calling the service you have to use in a new terminal (and in the workspace folder) the following command:
rosservice call /nodeB.

## Node C: 
It also is a service node that by retrieving the goal coordinates from the parameter (I did it with rospy.get_param(), but in comment I will explain another way that better exploits the power of services), with the function calc_dist_avg(req) it calculate the distance from the target and
It also subscribes to the '/pos_vel' topic and retrieve the message published by node A; this value are used for calculating the distance and average speed.

<img src="https://github.com/leleviola/rt1_assignment2/blob/resources/images/Schermata%20del%202024-01-13%2018-59-04.png" alt="Alt Text" width="1000"/>
## Prerequisites
You need to have installed the following programs:
- Gazebo: the 3d simulator for ros
- Rviz:a tool for ROS Visualization. It allows the user to view the simulated robot model, log sensor information from the robot's sensors, and replay the logged sensor information. By visualizing what the robot is seeing, thinking, and doing, the user can debug a robot application from sensor inputs to planned (or unplanned) actions.
- Xterm
- the code is written in python3, so, for running it, it's obviously needed it
- ROS (again... obviously)

## Running instructions

## Comments

Last commit 08 November 2023
