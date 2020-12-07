#!/usr/bin/env python

from colorama import Fore
import rospy
from sensor_msgs.msg import LaserScan, PointCloud2 ,PointField
from sensor_msgs import point_cloud2
from std_msgs.msg import Header
from math import cos, sin

# Global Var
pub = None

def callback(message):
    nmeasures = len(message.ranges)
    rospy.loginfo('I received "' + Fore.RED + str(nmeasures) + Fore.RESET + ' measurements')

    # Create point list
    points = []
    i = 0
    for range in message.ranges:
        theta = message.angle_min + i * message.angle_increment
        x = range * cos(theta)
        y = range * sin(theta)
        z = 0
        pt = [x, y, z]
        points.append(pt)
        i =+ 1

    # Message config
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1)
              ]
    header = Header()
    header.frame_id = "/left_laser/laserscan"
    pc2 = point_cloud2.create_cloud(header, fields, points)
    pub.publish(pc2)


def main():
    topic_name = 'chatter'
    rospy.init_node('Converter', anonymous=False)
    rospy.Subscriber(topic_name, LaserScan, callback)
    globals
    rospy.Publisher('~PointCloud2', PointCloud2, queue_size=10)

    rospy.spin()


if __name__ == '__main__':
    main()
