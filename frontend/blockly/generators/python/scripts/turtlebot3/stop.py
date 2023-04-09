seconds = "3"
dropdown_speed = "NORMAL"

import rospy, sys
import time
from geometry_msgs.msg import Twist

seconds = int(seconds) #added

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
try:
  rospy.init_node('circle_mode', anonymous=True)
except rospy.exceptions.ROSException as e:
    print("Node has already been initialized...")
rate = rospy.Rate(10) # 10Hz
twist = Twist()
movementTime = seconds
start = time.time()
flag=True #time flag
# Angular velocity = linear velocity / radius
speed=dropdown_speed # SLOW, NORMAL, FAST
twist.linear.z = 0.00

# CLOCKWISE rotation
if speed =='SLOW':
    twist.linear.y = 0.05
    twist.linear.x = 0.05
elif speed =='NORMAL':
    twist.linear.y = 0.25
    twist.linear.x = 0.25
elif speed == 'FAST':
    twist.linear.y = 0.75
    twist.linear.x = 0.75
while not rospy.is_shutdown() and flag:
    sample_time=time.time()
    if ((sample_time - start) > movementTime):
      flag=False
    pub.publish(twist)
twist = Twist()
pub.publish(twist)
rate.sleep()
dropdown_direction = "left"
degrees = "90"

import rospy, sys
import time
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import math

#diameter = 0.2 # meters
#radius = diameter/2;
#isFirst = True
#rotateRadians = rotateAngle * 0.0174533 # value to convert degrees to radians

try:
  rospy.init_node('circle_mode', anonymous=True)
except rospy.exceptions.ROSException as e:
    print("Node has already been initialized...")
msg_imu = rospy.wait_for_message('/odom', Odometry, timeout=3)
print(msg_imu.pose.pose.orientation)
quaternion = (
msg_imu.pose.pose.orientation.x,
msg_imu.pose.pose.orientation.y,
msg_imu.pose.pose.orientation.z,
msg_imu.pose.pose.orientation.w)

euler = euler_from_quaternion(quaternion)
initial_yaw = abs(math.degrees(euler[2]))

#rospy.init_node('turn_left', anonymous=True)
#rospy.Subscriber('/imu', Imu, handleImu)
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10) # 10Hz

twist = Twist()
flag=True
previous_yaw = initial_yaw
#loop = 0
degrees_change = 0


if "left" == dropdown_direction:
    direction = 1 # the factor that decides the turning left or right
    target = float(degrees)*0.95
elif "right" == dropdown_direction:
    direction = -1 # the factor that decides the turning left or right
    target = float(degrees)*1.05

while not rospy.is_shutdown() and flag:
    msg_imu = rospy.wait_for_message('/odom', Odometry, timeout=5)
    quaternion = (
    msg_imu.pose.pose.orientation.x,
    msg_imu.pose.pose.orientation.y,
    msg_imu.pose.pose.orientation.z,
    msg_imu.pose.pose.orientation.w)

    euler = euler_from_quaternion(quaternion)
    yaw = euler[2]
    yaw = math.degrees(yaw)
    yaw = abs(yaw)

    degrees_change += abs(previous_yaw - yaw)

    if (degrees_change < target):
        twist.angular.z = 0.5 * direction

    else:
        flag=False
        twist.angular.z = 0.0

    previous_yaw = yaw
    pub.publish(twist)

twist = Twist()
pub.publish(twist)
rate.sleep()

seconds = "4"
dropdown_speed = "SLOW"

import rospy, sys
import time
from geometry_msgs.msg import Twist

seconds = int(seconds) #added

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
try:
  rospy.init_node('circle_mode', anonymous=True)
except rospy.exceptions.ROSException as e:
    print("Node has already been initialized...")
rate = rospy.Rate(10) # 10Hz
twist = Twist()
movementTime = seconds
start = time.time()
flag=True #time flag
# Angular velocity = linear velocity / radius
speed=dropdown_speed # SLOW, NORMAL, FAST
twist.linear.z = 0.00

# CLOCKWISE rotation
if speed =='SLOW':
    twist.linear.y = 0.05
    twist.linear.x = 0.05
elif speed =='NORMAL':
    twist.linear.y = 0.25
    twist.linear.x = 0.25
elif speed == 'FAST':
    twist.linear.y = 0.75
    twist.linear.x = 0.75
while not rospy.is_shutdown() and flag:
    sample_time=time.time()
    if ((sample_time - start) > movementTime):
      flag=False
    pub.publish(twist)
twist = Twist()
pub.publish(twist)
rate.sleep()
