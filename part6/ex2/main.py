#! /usr/bin/python
import cv2
import numpy as np


def main():
    # setup
    window_name = 'Ex2'
    capture = cv2.VideoCapture(0)
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    _, image = capture.read()

    cv2.imshow(window_name, image)

    while True:
        key = cv2.waitKey(1)
        _, image = capture.read()
        cv2.imshow(window_name, image)
        if chr(key) == ' ':
            break


if __name__ == '__main__':
    main()
