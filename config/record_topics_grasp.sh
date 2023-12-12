rosbag record --split --size=500 -b 3000 \
/cmd_vel \
/detect_target \
/gr_land \
/grasp \
/grasp_mission_end \
/grasp_mission_retry \
/grasp_target_task_state \
/grasping_mission \
/imu/corrected \
/imu/filtered \
/imu/raw \
/imu/temperature \
/joint_states \
/odom/filtered \
/robot_angle \
/robot_on_target \
/sonar_dist \
/target_aligned \
/target_distance/x \
/target_distance/y \
/target_pose_from_robot
