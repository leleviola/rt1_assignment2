# Assignment 2: "3D Mobile Robot"

by leleviola

## Introduction
In this project there is a 3D simulator, in which there is mobile robot that moves in a plane, and an environment, a world, with edges and obstacles (walls); you can see  it in the picture below. The original package can bee seen here: https://github.com/CarmineD8/assignment_2_2023
I implemented other three nodes, that will be described in the next section:
- node A
- node B
- node C
During the simulation, there will be opened 5 windows, 2 are needed for the simulation, another one is the one from which you run the program, where there will be displayed som debug messagges, the other 2 are the nodeA and the nodeC
The robot has a laser sensor that permits to it to see obstacles in front of it, and has a cartesian coordinate sistem 
### Prerequisites
You need to have installed the following programs:
- Gazebo: the 3d simulation environment
- Rviz
- Xterm
- the code is written in python3, so, for running it, it's obviously needed it

## Steps and Pseudocode

The main program is composed by the robot initialization, where are initialized the most important variables, and by a while loop. This while loop is splitted in two sections:

- the first that contains all the actions that the robot do, when isn't grabbing any token, in order to take the nearest and right token;

- the second one that makes the robot release the token in the right place and starts if and only if the robot is moving a token.

<p>
  All the reasonings and steps are described in the flowchart below.
</p>

<p align= "center">
  <img src = "images/Flowchart.png">
  
  While markers is the variables that contains all the markers that the robot sees, marker_taken contains only the markers that are moved to the center. Doing this is easyer to determine wich of the markers that robot seen have been already moved and wich not.
  When the robot has to take a marker, it, using some function that will be described in the next section, checks if the token's distance is:
- =-1 => this means that the robot doesn't see any token;
- < a threshold value (0.4 or 0.6) => the robot grab/ungrab the token.
It also checks if the angle between the robot and the token is:
- -2 < angle < 2 => this means that the token is  straight in front of the robot so it has to toward it direction;
- major than 2 => turn right a bit
- minor than -2 => turn left a bit

**I should specify that solution is built under the condition that there are 6 token all placed in circle, this means that if they are more than 6 or not placed in circle it isn't sure that this solution will works**.
</p>

## Functions

For making coding simpler, I've used some useful functions.

### drive(speed, seconds)

Function for setting a linear velocity    
Args: 
  - speed (int): the speed of the wheels
  - seconds (int): the time interval
   
### turn(speed, seconds)

Function for setting an angular velocity    
Args: 
  - speed (int): the speed of the wheels
  - seconds (int): the time interval

### find_mindist_untaken_token(marker_list, marker_taken)

Function to find the closest token that is in marker_list and not in marker_taken
- Args:
  - marker_list(list): the list of all markers seen by the robot
  - marker_taken(list): the list of all the markers moved to the center
- Returns:
  - dist (float): distance of the closest token (-1 if no token is detected)
  - rot_y (float): angle between the robot and the token (-1 if no token is detected)
  - index (int): the index in marker_list of the token (-1 if no token is detected)

### find_mindist_taken_token(marker_list, marker_taken)

Function to find the closest token of tokens that are in marker_list and also in marker_taken
- Args:
  - marker_list(list): the list of all markers seen by the robot
  - marker_taken(list): the list of all the markers moved to the center
- Returns:
  - dist (float): distance of the closest token (-1 if no token is detected)
  - rot_y (float): angle between the robot and the token (-1 if no token is detected)
  - index (int): the index in marker_list of the token (-1 if no token is detected)
### find_maxdist_token(marker_list)
Function to find of the most distant token
- Args:
  - marker_list(list): the list of all markers seen by the robot

- Returns:
  - dist (float): distance (-1 if no token is detected)
  - rot_y (float): angle between the robot and the token (-1 if no token is detected)
  - index(int): the index of the element at max distance
 
### find_same_token(list, mark)
    
Function to determine if there is the token "mark" in the list of tokens "list".
- Args:
  - list(list): is the list where it will search the token "mark"
  - mark(Token): is the token to find
- Returns:
  - True if "mark" is in "list"
  - False if "mark" isn't in "list"

## Results and conclusions
After having traveled the entire circle, and having moved all the tokens together, the robot should print a message in terminal and stop moving, and all the tokens are like in the following image. 
<p align = "center">
  <img src ="images/End.png">
</p>
Last commit 08 November 2023
