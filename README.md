# Prepare lib to working with kinect

In ubuntu 20.04.2 LTS :


Clone code from: 

```
git clone https://github.com/OpenKinect/libfreenect
```

Edit comment from line 443 to 452 in the file:

```
libfreenect/src/usb_libusb10.c
```

Install the next packages

```
apt-get install build-essential
apt-get install git-core cmake freeglut3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev

```

Install cython and opencv:

```
sudo python3 -m pip install cython
sudo python3 -m pip install opencv-contrib-python
```

Compile and install:

```
mkdir build
cd build
cmake .. -DBUILD_PYTHON3=ON
make 
sudo make install
```

update path
```
sudo ldconfig
```
In a directory copy freenect.so located at:

```
libfreenect/build/wrappers/python/python3
```

Write this example, save: demo_kinect.py  :

```
#!/usr/bin/env python
"""
file: demo_kinect.py 
Ing. Noé Vásquez Godínez
Miércoles Julio 07 2021 ,01:36:49
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

```

Your test directory should contain the following:
```
ziusudra@ziusudra:~/Desktop/kinect$ tree .
.
├── demo_kinect.py
└── freenect.so
```

Execute :

```
sudo python3 demo_kinect.py 
```
