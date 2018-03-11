import cv2
import ImageProcessing
from ImageProcessing import Pixel
from ImageProcessing import PProcessing
from StructBuilder import StructBuilder
import numpy as np

WIDTH = 400
HEIGHT = 400
DETECTORS = 3
DELTHA_ANGLE = 20
DETECTORS_WIDTH = 30

ImgProc = PProcessing()
structBuilder = StructBuilder(WIDTH, HEIGHT, DELTHA_ANGLE, DETECTORS, DETECTORS_WIDTH)

img = cv2.imread('res/image_01.png')
img = cv2.resize(img, (400, 400))

for o in structBuilder.circle:
    cv2.circle(img, (int(o.x), int(o.y)), 2, (0, 0, 255), -1)

line = ImgProc.bresenhamLine(0,0,100,100)

#structBuilder.createRays()
print(structBuilder.rays)

cv2.imshow('Tomograf', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

