
import rospy, sys
import time
from geometry_msgs.msg import Twist

seconds = int(seconds) #added

diameter = 0.2 # meters
radius = diameter/2;
try:
  rospy.init_node('circle_mode', anonymous=True)
except rospy.exceptions.ROSException as e:
    print("Node has already been initialized...")
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
# rospy.init_node('turn_left', anonymous=True) #uncommented
rate = rospy.Rate(10) # 10Hz
twist = Twist()
movementTime = seconds
start = time.time()
flag=True #time flag
# Angular velocity = linear velocity / radius
speed=dropdown_speed # SLOW, NORMAL, FAST
twist.linear.x = 0.0
twist.linear.z = 0.0

# CLOCKWISE rotation
if speed =='SLOW':
    twist.linear.y = 0.05
    twist.angular.z = twist.linear.y/radius
elif speed =='NORMAL':
    twist.linear.y = 0.25
    twist.angular.z = twist.linear.y/radius
elif speed == 'FAST':
    twist.linear.y = 0.75
    twist.angular.z = twist.linear.y/radius
while not rospy.is_shutdown() and flag:
    sample_time=time.time()
    if ((sample_time - start) > movementTime):
      flag=False
    pub.publish(twist)
twist = Twist()
pub.publish(twist)
rate.sleep()

