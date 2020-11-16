#!/usr/bin/env python
import cv2
import argparse
import numpy

from readchar import readkey

# load starting colour
colour = (0, 0, 255)
image = numpy.ones((400, 600, 3), numpy.uint8) * 255


def onMouse(q, w, e, r, t):
    if q == 1:
        center = (w, e)

        draw(image, center, colour)


def draw(image, center, colour):
    radius = 2
    cv2.circle(image, center, radius, colour, thickness=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, help='Full path to image file.')
    args = vars(parser.parse_args())

    window_name = 'window - Ex1a'
    if args['image']:
        global image
        image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image



    while True:
        global image
        cv2.imshow(window_name, image)
        cv2.setMouseCallback(window_name, onMouse, image)

        # key based options
    #    key_pressed = readkey()
    #    global colour
    #    if key_pressed = 'r':
    #        # select red colour
    #        colour = (0, 0, 255)
    #    elif key_pressed = 'g':
    #        # select green colour
    #        colour = (0, 255, 0)
    #    elif key_pressed = 'b':
    #        # select blue colour
    #        colour = (255, 0, 0)
    #    elif key_pressed = 't':
    #        # select text box
    #    elif key_pressed = 'e':
    #        # exit program

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
