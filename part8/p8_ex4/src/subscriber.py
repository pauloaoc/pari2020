#!/usr/bin/env python

import argparse
from colorama import Fore
import rospy
from std_msgs.msg import String
from p8_ex4.msg import Dog


def messageRecivedCallback(message):
    rospy.loginfo('recived message: "' + Fore.RED + str(message) + Fore.RESET + '"')


def main():
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('-tn', '--topic_name', type=str, default='chatter', help='Name...')
    args = vars(parser.parse_args())

    rospy.init_node('Subscriber', anonymous=True)
    rospy. Subscriber(args['topic_name'], Dog, messageRecivedCallback)

    rospy.spin()


if __name__ == '__main__':
    main()