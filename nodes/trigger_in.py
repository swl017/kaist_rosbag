#!/usr/bin/env python

'''
@date: 2021-08-17
@author: Seungwook Lee, KAIST
@source: https://gist.github.com/marco-tranzatto/8be49b81b1ab371dcb5d4e350365398a
'''

import rospy
import subprocess
import os
import signal

from std_msgs.msg import Bool


class RosbagRecord:
    def __init__(self):
        if rospy.has_param('~record_script') and rospy.has_param('~record_folder'):
            self.record_script = rospy.get_param('~record_script')
            self.record_folder = rospy.get_param('~record_folder')
        else:
            rospy.signal_shutdown(rospy.get_name() + ' no record script or folder specified.')

        self.trigger_topic_name = rospy.get_param('~trigger_topic_name')
        self.trigger_timeout = rospy.get_param('~trigger_timeout')
        self.verbose = rospy.get_param('~verbose')
        rospy.loginfo("trigger topic name: "+self.trigger_topic_name)
        
        self.trigger_topic_subscriber = rospy.Subscriber(self.trigger_topic_name, Bool, self.trigger_subscriber_callback)
        
        self.prev_in = 0.0
        self.last_trigger = False

    def terminate_ros_node(self, s):
        # Adapted from http://answers.ros.org/question/10714/start-and-stop-rosbag-within-a-python-script/
        list_cmd = subprocess.Popen("rosnode list", shell=True, stdout=subprocess.PIPE)
        list_output = list_cmd.stdout.read()
        retcode = list_cmd.wait()
        assert retcode == 0, "List command returned %d" % retcode
        for str in list_output.split("\n"):
            if (str.startswith(s)):
                os.system("rosnode kill " + str)

    def start_recording_handler(self):
        # Start recording.
        command = "source " + self.record_script 
        self.p = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=self.record_folder,
                                    executable='/bin/bash')


    def stop_recording_handler(self):
        rospy.loginfo(rospy.get_name() + ' stop recording.')
        self.terminate_ros_node("/record")

    def trigger_subscriber_callback(self, msg):
        self.prev_in = rospy.get_time()

    def run(self):
        if(self.verbose):
            rospy.loginfo("Recieving trgger")
        if(rospy.get_time() - self.prev_in) < self.trigger_timeout and self.last_trigger == False:
            self.last_trigger = True
            rospy.loginfo("Start rosbag")
            self.start_recording_handler()
        elif(rospy.get_time() - self.prev_in) >= self.trigger_timeout and self.last_trigger == True:
            self.last_trigger = False
            rospy.loginfo("Stop rosbag")
            self.stop_recording_handler()

if __name__ == '__main__':
    rospy.init_node('rosbag_record')
    rospy.loginfo(rospy.get_name() + '.py start')

    try:
        rosbag_record = RosbagRecord()
        while not rospy.is_shutdown():
            rosbag_record.run()
	rospy.on_shutdown(rosbag_record.stop_recording_handler)
    except Exception as e:
        rospy.logerr(str(e))