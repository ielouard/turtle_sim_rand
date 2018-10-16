# Turtle_sim_rand
Basic ROS Publisher/Subscriber and Service example

To run the package follow those steps:

>If you already have a workspace skip step 0

0. To create a workspace follow this tutorial http://wiki.ros.org/catkin/Tutorials/create_a_workspace
1. Make sure you are in <your_ros_workspace>/src 
    ```sh
     $ cd <your_ros_workspace>/src 
    ```
2. Clone the repositorie into your workspace
    ```sh
     $ git clone https://github.com/ielouard/turtle_sim_rand.git
    ```
3. go back to your worspace directory then do a catkin_make and source your devel/setup.bash
    ```sh
     $ cd ~/<your_ros_workspace>
     $ catkin_make
     $ source devel/setup.bash
    ```
4. Finally, run the package
    ```sh
     $ roslaunch turtle_sim_rand turtlsim.launch 
    ```
