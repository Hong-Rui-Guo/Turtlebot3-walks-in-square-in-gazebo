#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


if __name__=="__main__":

    rospy.init_node('turtlebot3_square')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
    twist = Twist()

    rate = rospy.Rate(1) # 1hz
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
        angular_vel = -0.3
        twist.linear.x = linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = angular_vel


        while ( (rospy.get_time() - start_time) < 5):
            pub.publish(twist)
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
            break



