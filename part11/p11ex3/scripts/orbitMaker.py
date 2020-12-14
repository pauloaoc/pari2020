#!/usr/bin/env python

# Imports:
import rospy
from math import cos, sin, pi
import tf_conversions
import tf2_ros


# Main:
def main():
    rospy.init_node('Orbit')
    br = tf2_ros.TransformBroadcaster()
    t = tf2_ros.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = rospy.get_param('~parent')

    vel = rospy.get_param('~velocity') * 0.001
    raio = rospy.get_param('~radius')
    vel_rot = rospy.get_param('~vel_rot')
    angulo = 0
    t.child_frame_id = rospy.get_param('~child')
    rot = 0

    while not rospy.is_shutdown():
        # Polar coordinates:
        t.transform.translation.x = raio * cos(angulo)
        t.transform.translation.y = raio * sin(angulo)
        t.transform.translation.z = 0

        q = tf_conversions.transformations.quaternion_from_euler(0, 0, rot)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        t.header.stamp = rospy.Time.now()
        br.sendTransform(t)

        angulo += vel
        rot += vel_rot
        rospy.sleep(0.05)

        if angulo > 2 * pi:
            angulo = 0

        if rot > 2 * pi:
            rot = 0
    rospy.spin()


if __name__ == '__main__':
    main()
