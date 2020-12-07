#!/usr/bin/env python


from colorama import Fore
import rospy
from p8_ex4.msg import Dog


def messageRecivedCallback(message):
    rospy.loginfo('recived message: "' + Fore.RED + str(message) + Fore.RESET + '"')


def main():
    topic_name= 'chatter'
    rospy.init_node('Subscriber', anonymous=True)
    rospy. Subscriber(topic_name, Dog, messageRecivedCallback)

    rospy.spin()


if __name__ == '__main__':
    main()