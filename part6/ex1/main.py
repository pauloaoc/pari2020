#!/usr/bin/env python
import cv2
import argparse
import numpy

from readchar import readkey


def onMouse(q, w, e, r, t, colour, image):
    if q == 1:
        image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, help='Full path to image file.')
    args = vars(parser.parse_args())

    window_name = 'window - Ex1a'
    if args['image']:
        image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    else:
        image = numpy.ones((400, 600, 3), numpy.uint8) * 255

    # starting image
    cv2.imshow(window_name, image)

    # load starting colour
    colour = (0, 0, 255)

    print (type(image))
    # draw function
#    cv2.setMouseCallback(window_name, onMouse(colour=colour, image=image))

#    #key based options
#    key_pressed = readkey()
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