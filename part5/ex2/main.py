#!/usr/bin/env python

import cv2

def main():
    image = cv2.imread('./pari_20-21/Parte05/images/atlas2000_e_atlasmv.png')
    window_name = 'my_window'
    cv2.imshow(window_name, image)

if __name__ == "__main__":
    main()