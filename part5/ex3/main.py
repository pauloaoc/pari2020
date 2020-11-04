#!/usr/bin/env python
import argparse
import cv2

# Global variables
#window_name = 'window - Ex3a'
#image_gray = None
from functools import partial


def onTrackbar(threshold, image_gray, window_name):
    _, return_image = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, return_image)

def onMouse(q, w, e, r, t):
    if q == 1:
        print(w, e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    window_name = 'window - Ex3a'
    #image_gray = None

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    #global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    cv2.createTrackbar('threshold', window_name, 128, 255, partial(onTrackbar, image_gray=image_gray, window_name=window_name))
    onTrackbar(128, image_gray, window_name)

    # 3c
    cv2.setMouseCallback(window_name, onMouse)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()