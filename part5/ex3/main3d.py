#!/usr/bin/env python
import argparse
import cv2

# Global variablesgit sta
#window_name = 'window - Ex3a'
#image_gray = None
import json
from functools import partial


def onTrackbarBHH(bhh, limits, image, window_name):
    # build limits
    limits['BH']['max'] = bhh
    imageProcessor(limits, image, window_name)

def onTrackbarBHL(bhl, limits, image, window_name):
    # build limits
    limits['BH']['min'] = bhl
    imageProcessor(limits, image, window_name)

def onTrackbarGSH(gsh, limits, image, window_name):
    # build limits
    limits['GS']['max'] = gsh
    imageProcessor(limits, image, window_name)

def onTrackbarGSL(gsl, limits, image, window_name):
    # build limits
    limits['GS']['min'] = gsl
    imageProcessor(limits, image, window_name)

def onTrackbarRVH(rvh, limits, image, window_name):
    # build limits
    limits['RV']['max'] = rvh
    imageProcessor(limits, image, window_name)

def onTrackbarRVL(rvl, limits, image, window_name):
    # build limits
    limits['RV']['min'] = rvl
    imageProcessor(limits, image, window_name)

def imageProcessor(limits, image, window_name):
    # build limits
    low = (limits['BH']['min'], limits['GS']['min'], limits['RV']['min'])
    high = (limits['BH']['max'], limits['GS']['max'], limits['RV']['max'])

    print(low, high)
    # colour mask
    mask_bin = cv2.inRange(image, low, high)
    cv2.imshow(window_name, mask_bin)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    parser.add_argument('-HSV', '--HSV_image_mode', action="store_true", help='Default BGR, if active image will be '
                                                                              'processed by HSV')
    args = vars(parser.parse_args())

    # Define dictionary
    start_high = 255
    start_low = 0
    limits = {'BH': {'max': start_high, 'min': start_low}, 'GS': {'max': start_high, 'min': start_low}, 'RV': {'max': start_high, 'min': start_low}}

    # Load image and original image print
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    cv2.imshow('Original image',image)

    # Process image
    if args['HSV_image_mode']:
        window_name = 'HSV-Mask'
        image_to_process = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    else:
        window_name = 'BGR-Mask'
        image_to_process = image.copy()

    cv2.namedWindow(window_name)
    cv2.createTrackbar('thresholdBHH', window_name, start_high, 255, partial(onTrackbarBHH, limits=limits, image=image_to_process, window_name=window_name))
    onTrackbarBHH(start_high, limits, image_to_process, window_name)
    cv2.createTrackbar('thresholdBHL', window_name, start_low, 255, partial(onTrackbarBHL, limits=limits, image=image_to_process, window_name=window_name))
    onTrackbarBHL(start_low, limits, image_to_process, window_name)

    cv2.createTrackbar('thresholdGSH', window_name, start_high, 255, partial(onTrackbarGSH, limits=limits, image=image_to_process, window_name=window_name))
    onTrackbarGSH(start_high, limits, image_to_process, window_name)
    cv2.createTrackbar('thresholdGSL', window_name, start_low, 255, partial(onTrackbarGSL, limits=limits, image=image_to_process, window_name=window_name))
    onTrackbarGSL(start_low, limits, image_to_process, window_name)

    cv2.createTrackbar('thresholdRVH', window_name, start_high, 255, partial(onTrackbarRVH, limits=limits, image=image_to_process, window_name=window_name))
    onTrackbarRVH(start_high, limits, image_to_process, window_name)
    cv2.createTrackbar('thresholdRVL', window_name, start_low, 255, partial(onTrackbarRVL, limits=limits, image=image_to_process, window_name=window_name))
    onTrackbarRVL(start_low, limits, image_to_process, window_name)
    cv2.waitKey(0)

    # print limits to a txt
    file_name = 'limits.json'
    with open(file_name, 'w') as file_handle:
        print('writing dictionary d to file ' + file_name)
        json.dump(limits, file_handle)  # d is the dicionary



if __name__ == '__main__':
    main()