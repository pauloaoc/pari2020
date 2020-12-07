#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from colorama import Fore
# from dog_lib import Dog
from p8_ex4.msg import Dog


def main():
    topic_name = 'chatter'

    pub = rospy.Publisher(topic_name, Dog, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    frequency = rospy.get_param('~freq', 1)

    rate = rospy.Rate(frequency)

    dog_msg = Dog()
    dog_msg.name = 'Bobi'
    dog_msg.age = 7
    dog_msg.color = 'Black'
    dog_msg.brothers.append('Lassie')

    while not rospy.is_shutdown():
        rospy.loginfo('Publishing messege: ' + Fore.RED + str(dog_msg) + Fore.RESET
                      + '" on topic ' + rospy.remap_name(topic_name))
        pub.publish(dog_msg)
        rate.sleep()


if __name__ == '__main__':
    main()
