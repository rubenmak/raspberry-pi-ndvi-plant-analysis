

import sys
import time
import numpy as np
import cv2
import picamera
import picamera.array

def label(image, text):
    """
    Labels the given image with the given text
    """
    return cv2.putText(image, text, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)


def contrast_stretch(im):
    """
    Performs a simple contrast stretch of the given image, from 5-100%.
    """
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 100)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out


def run():
    with picamera.PiCamera() as camera:
        # Set the camera resolution
        x = 400
        camera.resolution = (int(1.33 * x), x)
        # Various optional camera settings below:
        # camera.framerate = 5
        # camera.awb_mode = 'off'
        # camera.awb_gains = (0.5, 0.5)
        camera.hflip = True
        camera.vflip = True
        if len(sys.argv) == 2:
            camera.rotation = sys.argv[1]

        # Need to sleep to give the camera time to get set up properly
        time.sleep(1)

        with picamera.array.PiRGBArray(camera) as stream:
            # Loop constantly
            while True:
                # Grab data from the camera, in colour format
                # NOTE: This comes in BGR rather than RGB, which is important
                # for later!
                camera.capture(stream, format='bgr', use_video_port=True)
                image = stream.array

                # Get the individual colour components of the image
                b, g, r = cv2.split(image)

                # Calculate the NDVI
                bottom = (r.astype(float) + b.astype(float))
                bottom[bottom == 0] = 0.00001  # Make sure we don't divide by zero!

                ndvi = (r.astype(float) - b) / bottom
                ndvi = contrast_stretch(ndvi)
                ndvi = ndvi.astype(np.uint8)

                # Do the labelling
                label(image, 'original')
                label(ndvi, 'NDVI')

                # Display
                cv2.imshow('NDVI Image', ndvi)
                cv2.imshow('Original Image', image)

                stream.truncate(0)

                # If we press ESC then break out of the loop
                c = cv2.waitKey(7) % 0x100
                if c == 27:
                    break

    # Important cleanup here!
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run()
