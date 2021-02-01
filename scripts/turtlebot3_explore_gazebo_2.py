#!/usr/bin/env python

import math
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler


def get_rotation (msg):
    global roll, pitch, yaw
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    # print(yaw)



if __name__=="__main__":

    rospy.init_node('turtlebot3_square')

    # publisher
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
    twist = Twist()

    # subscriber
    sub = rospy.Subscriber ('/odom', Odometry, get_rotation)

    # euler angle
    roll = 0.0
    pitch = 0.0
    yaw = 0.0


    rate = rospy.Rate(3) # 3hz
    count = 0

    # control for first time
    start_time = rospy.get_time()

    while ( (rospy.get_time() - start_time) < 3):
        twist_str = "wait for 3 seconds"
        rospy.loginfo(twist_str)
        rate.sleep()


    while not rospy.is_shutdown():

        # go through for 5 seconds
        start_time = rospy.get_time()
        linear_vel = 0.1
        angular_vel = 0.0
        twist.linear.x = linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = angular_vel

        while ( (rospy.get_time() - start_time) < 5):
            pub.publish(twist)
            twist_str = "go through"
            rospy.loginfo(twist_str)
            rate.sleep()

        # stop
        start_time = rospy.get_time()
        linear_vel = 0.0
        angular_vel = 0.0
        twist.linear.x = linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = angular_vel

        while ( (rospy.get_time() - start_time) < 3):
            pub.publish(twist)
            twist_str = "stop"
            rospy.loginfo(twist_str)
            rate.sleep()

        # turn right
        start_time = rospy.get_time()
        linear_vel = 0.0
        angular_vel = -0.1
        twist.linear.x = linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = angular_vel

        # get start yaw
        # rospy.spinonce()
        start_yaw = yaw
        print('start yaw')
        print(start_yaw)
        rospy.loginfo('math.pi')
        rospy.loginfo(math.pi)

        while ( abs(start_yaw - yaw) < math.pi/2):
            pub.publish(twist)
            # rospy.spinonce()
            print('current yaw')
            print(yaw)
            twist_str = "turn right"
            rospy.loginfo(twist_str)
            rate.sleep()

        # determinate whether turtlebot walk square
        count = count + 1
        if count == 4:
            linear_vel = 0.0
            angular_vel = 0.0
            twist.linear.x = linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = angular_vel

            pub.publish(twist)
            twist_str = "finish"
            rospy.loginfo(twist_str)
            # print('test')

            break



