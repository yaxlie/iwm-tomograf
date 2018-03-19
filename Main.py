import cv2
from PIL import Image
from skimage.color import rgb2gray

import ImageProcessing
from ImageProcessing import Pixel
from ImageProcessing import PProcessing
from StructBuilder import StructBuilder
import time
from matplotlib import pyplot as plt
import numpy as np

WIDTH = 400
HEIGHT = 400
DETECTORS = 12
DELTHA_ANGLE = 2
DETECTORS_WIDTH = 30
IMG_PATH = 'res/image_01.png'

imgProc = PProcessing()
structBuilder = StructBuilder(WIDTH, HEIGHT, DELTHA_ANGLE, DETECTORS, DETECTORS_WIDTH)


imgGrey = rgb2gray(cv2.imread(IMG_PATH))
img = cv2.imread(IMG_PATH)
img = cv2.resize(img, (400, 400))

for o in structBuilder.circle:
    cv2.circle(img, (int(o.x), int(o.y)), 2, (0, 0, 255), -1)

line = imgProc.bresenhamLine(0,0,100,100)
imgOrigin = np.copy(img)

cv2.imshow('Tomograf', img)

time.sleep(2)
structBuilder.createRays()

# print(structBuilder.getMeanFromRay(0, imgGrey))
# print(imgGrey[0][0])

sinogram = []

for rays in structBuilder.rays:
    # print(structBuilder.getMeanFromRay(rays, imgGrey))
    sinogram.append(structBuilder.getMeanFromRay(rays, imgGrey))
    img = np.copy(imgOrigin)
    for ray in rays:
        for pixel in ray.pixels:
            cv2.circle(img, (int(pixel.x), int(pixel.y)), 1, (0, 255, 0), -1)

    cv2.imshow('Tomograf', img)
    cv2.waitKey(1)
    time.sleep(0.01)


# print(np.asarray(sinogram))
# print(imgGrey)

h = min(map(len, sinogram))
w = len(sinogram)
new_img = np.zeros([h, w, 3], dtype=np.uint8)
new_img = rgb2gray(new_img)

print(w, h)

for i in range(0, h):
    for j in range(0,w):
        # print(i," ", j," ", sinogram[j][i])
        new_img[i][j] = sinogram[j][i]

# print(np.asarray(new_img))

cv2.imshow('Sinogram', new_img)

cv2.imshow('Tomograf', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

