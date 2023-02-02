# kaist_rosbag

- Automatically starts recording `rosbag` according to what's stated in [`config/command_line_rosbag_record.sh`](config/command_line_rosbag_record.sh)
- Specify the trigger message in [`launch/kaist_rosbag.launch`](launch/kaist_rosbag.launch)

- Launch command:
    ```bash
    roslaunch kaist_rosbag kaist_rosbag.launch
    ```