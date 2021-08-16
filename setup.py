from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
  scripts=['nodes/kaist_rosbag.py'],
  requires=['std_msgs', 'rospy']
)

setup(**d)