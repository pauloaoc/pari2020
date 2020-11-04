#!/usr/bin/env python

import cv2
import numpy as np


def main():
    imageRGB = cv2.imread('../images/atlascar2.png', 1)
    image = cv2.cvtColor(imageRGB, cv2.COLOR_BGR2GRAY)
    image_thresholded = image > 128
    image_thresholded = image_thresholded.astype(np.uint8) * 255
    window_name = 'Bin'
    #cv2.imshow(window_name, image_thresholded)
    # print (type(image_thresholded))
    # print (image_thresholded.shape)
    # print (image_thresholded.dtype)
    imageB, imageR, imageG = cv2.split(imageRGB)
    _, imageB = cv2.threshold(imageB, 50, 255, cv2.THRESH_BINARY)
    _, imageR = cv2.threshold(imageR, 100, 255, cv2.THRESH_BINARY)
    _, imageG = cv2.threshold(imageG, 100, 255, cv2.THRESH_BINARY)
    rgbin = cv2.merge((imageB, imageR, imageG))
    #cv2.imshow('Color_Bin', rgbin)
    #cv2.waitKey(0)

    # 2d)
    imageRGB1 = cv2.imread('../images/atlas2000_e_atlasmv.png', 1)
    # Boundaries:
    maxlim = (40, 255, 40)
    minlim = (0, 70, 0)
    maskbin = cv2.inRange(imageRGB1, minlim, maxlim)
    #cv2.imshow('Mask_1', maskbin)
    #cv2.waitKey(0)

    # 2 e)
    image_hsv = cv2.cvtColor(imageRGB1, cv2.COLOR_BGR2HSV)
    maxlim = (100, 255, 255)
    minlim = (50, 100, 70)
    maskbin2 = cv2.inRange(image_hsv, minlim, maxlim)
    #cv2.imshow('Mask_2', maskbin2)
    #cv2.imshow('OG_2', imageRGB1)
    #cv2.waitKey(0)

    # 2 f)
    maxlim = (40, 255, 40)
    minlim = (0, 60, 0)
    maskbox = cv2.inRange(imageRGB1, minlim, maxlim)
    redbox = imageRGB1
    cv2.add(imageRGB1, (0,0,255,0), dst = redbox, mask = maskbox)
    cv2.imshow('cor',redbox)
    cv2.waitKey()
if __name__ == "__main__":
    main()
