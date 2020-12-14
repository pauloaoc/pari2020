#!/usr/bin/env python


from functools import partial
from math import cos, sin
import rospy
from std_msgs.msg import Header, ColorRGBA
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import MarkerArray, Marker
from geometry_msgs.msg import Point
from matplotlib import cm


def laserMsgCalback(msg, publisher):
    rospy.loginfo('Received LaserScan msg')

    # initialize a marker for publishing
    marker = Marker()
    marker.header.frame_id = msg.header.frame_id
    marker.header.stamp = msg.header.stamp
    marker.ns = "clusters"
    marker.id = 0
    marker.type = Marker.POINTS
    marker.action = Marker.ADD
    marker.pose.orientation.w = 1.0
    marker.scale.x = 0.1
    marker.scale.y = 0.1
    marker.scale.z = 1

    threshold_max_range_dif = 0.5
    cluster_idx = 0
    points_cluster = []

    # Calculate number of clusters
    for idx, r in enumerate(msg.ranges):
        if abs(r - msg.ranges[idx - 1]) > threshold_max_range_dif and idx != 0:
            cluster_idx += 1
        points_cluster.append(cluster_idx)

    # initialize clusters and color map

    colormap = cm.tab20(range(0, cluster_idx + 1))

    for idx, r in enumerate(msg.ranges):
        theta = msg.angle_min + idx * msg.angle_increment
        x, y = r * cos(theta), r * sin(theta)

        point = Point(x=x, y=y, z=0)
        marker.points.append(point)

        color = ColorRGBA(r=colormap[points_cluster[idx], 0],
                          g=colormap[points_cluster[idx], 1],
                          b=colormap[points_cluster[idx], 2],
                          a=1)
        marker.colors.append(color)

    marker_array = MarkerArray()
    marker_array.markers.append(marker)
    publisher.publish(marker_array)
    rospy.loginfo('Published MarkerArray with clusters')


def main():
    rospy.init_node('lidar_clustering', anonymous=False)

    publisher = rospy.Publisher('~/cluster', MarkerArray, queue_size=1)

    rospy.Subscriber('/left_laser/laserscan', LaserScan, partial(laserMsgCalback, publisher=publisher))

    rospy.spin()

if __name__ == '__main__':
    main()