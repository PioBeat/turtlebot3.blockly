
import rospy, sys
import time
from geometry_msgs.msg import Twist

diameter = 0.2 # meters
radius = diameter/2;
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
try:
  rospy.init_node('circle_mode', anonymous=True)
except rospy.exceptions.ROSException as e:
    print("Node has already been initialized...")
rate = rospy.Rate(10) # 10Hz
twist = Twist()
start = time.time()
flag=True #time flag

speed=dropdown_speed # SLOW, NORMAL, FAST
direction=dropdown_direction # CLOCKWISE, COUNTER-CLOCKWISE
twist.linear.x = 0.0
twist.linear.z = 0.0

# CLOCKWISE rotation
if speed =='SLOW' and direction =='CLOCKWISE':
	twist.linear.y = -0.05
	twist.angular.z = twist.linear.y/radius # Angular velocity = linear velocity / radius
elif speed =='NORMAL' and direction =='CLOCKWISE':
	twist.linear.y = -0.25
	twist.angular.z = twist.linear.y/radius 
elif speed == 'FAST' and direction =='CLOCKWISE':
	twist.linear.y = -0.75
	twist.angular.z = twist.linear.y/radius

# COUNTER-CLOCKWISE rotation
elif speed =='SLOW' and direction =='COUNTER-CLOCKWISE':
	twist.linear.y = 0.05
	twist.angular.z = twist.linear.y/radius 
elif speed =='NORMAL' and direction =='COUNTER-CLOCKWISE':
	twist.linear.y = 0.25
	twist.angular.z = twist.linear.y/radius 
elif speed == 'FAST' and direction =='COUNTER-CLOCKWISE':
	twist.linear.y = 0.75
	twist.angular.z = twist.linear.y/radius
 
while not rospy.is_shutdown() and flag:
    sample_time=time.time()
    if ((sample_time - start) > 3):
      flag=False
    pub.publish(twist)
twist = Twist()
pub.publish(twist)
rate.sleep()
