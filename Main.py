import cv2
import ImageProcessing
from ImageProcessing import Pixel
from ImageProcessing import PProcessing
from StructBuilder import StructBuilder
import time
from matplotlib import pyplot as plt
import numpy as np

WIDTH = 400
HEIGHT = 400
DETECTORS = 6
DELTHA_ANGLE = 20
DETECTORS_WIDTH = 30

imgProc = PProcessing()
structBuilder = StructBuilder(WIDTH, HEIGHT, DELTHA_ANGLE, DETECTORS, DETECTORS_WIDTH)

img = cv2.imread('res/image_01.png')
img = cv2.resize(img, (400, 400))

for o in structBuilder.circle:
    cv2.circle(img, (int(o.x), int(o.y)), 2, (0, 0, 255), -1)

line = imgProc.bresenhamLine(0,0,100,100)
imgOrigin = np.copy(img)

cv2.imshow('Tomograf', img)

time.sleep(2)
structBuilder.createRays()
for rays in structBuilder.rays:
    img = np.copy(imgOrigin)
    for ray in rays:
        for pixel in ray.pixels:
            cv2.circle(img, (int(pixel.x), int(pixel.y)), 1, (0, 255, 0), -1)

    cv2.imshow('Tomograf', img)
    cv2.waitKey(1)
    time.sleep(1)

cv2.imshow('Tomograf', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

