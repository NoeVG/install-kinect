#!/usr/bin/env python
"""
Ing. Noé Vásquez Godínez
Miércoles Julio 07 01:36:49
"""

# Import kinect
import freenect

# Import opencv 
import cv2

# Import numpy structures
import numpy as np


def get_video():
    """ Function to get RGB image from kinect """
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

def get_depth():
    """ Function to get depth image from kinect """
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    return array

if __name__ == "__main__":
    """ The main function """
    while True:
        # Get a frame from RGB camera
        frame = get_video()

        # Get a frame from depth sensor
        depth = get_depth()

        # Display RGB image
        cv2.imshow('RGB image',frame)

        # Display depth image
        cv2.imshow('Depth image',depth)

        # Quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF

        if k == 27:
            break

    cv2.destroyAllWindows()
