#!/usr/bin/env python

import argparse
import rospy
from std_msgs.msg import String
from colorama import Fore
from dog_lib import Dog


def main():
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('-tn', '--topic_name', type=str, default='chatter', help='Name...')
    parser.add_argument('-m', '--message_content', type=str, default='Nothing to say!',
                        help='content of the message to publish.')
    parser.add_argument('-f', '--frequency', type=float, default=10, help='frequency of publications (Hz)')
    args = vars(parser.parse_args())

    pub = rospy.Publisher(args['topic_name'], String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(args['frequency'])

    dog = Dog(name='Bobi', age=7, color='black')
    dog.addBrother('Lassie')

    while not rospy.is_shutdown():
        rospy.loginfo('Publishing messege: ' + Fore.RED + args['message_content'] + Fore.RESET
                      + '" on topic ' + args['topic_name'])
        pub.publish(args['message_content'])
        rate.sleep()


if __name__ == '__main__':
    main()