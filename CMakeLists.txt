cmake_minimum_required(VERSION 3.0.2)
project(kaist_rosbag)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package(
 CATKIN_DEPENDS rospy
)

catkin_python_setup()

install(PROGRAMS
  nodes/kaist_rosbag.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  FILES_MATCHING PATTERN "*.launch" PATTERN "*.yaml" PATTERN "*.sh"
)

install(DIRECTORY config/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
  FILES_MATCHING PATTERN "*.yaml" PATTERN "*.sh"
)