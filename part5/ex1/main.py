#!/usr/bin/env python
import cv2
import argparse
import time


def main():
    parser = argparse.ArgumentParser(description='Show selected image')
    parser.add_argument('-p', '--path', type=str, default='../images/atlascar.png',
                        help='type the directory of the image you want (default: ../images/atlascar.png)')
    args = parser.parse_args()

    image = cv2.imread('../images/atlas2000_e_atlasmv.png')
    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(3000)
    #time.sleep(3)

    image_filename = args.path
    image = cv2.imread(image_filename) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()