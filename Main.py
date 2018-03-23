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

WIDTH = 600
HEIGHT = 600
DETECTORS = 40
DELTHA_ANGLE = 12
DETECTORS_WIDTH = 90
ITERATIONS = 60

#zmiana dokladnosci punktów. np. dla accuracy = 2 -> 1 stopien = 1/2 stopnia
# -> zamiast 360, 720 punktów okręgu
ACCURACY = 4

IMG_PATH = 'res/image_04.png'

imgProc = PProcessing()
structBuilder = StructBuilder(WIDTH, HEIGHT, DELTHA_ANGLE, DETECTORS,
                              DETECTORS_WIDTH, ACCURACY, ITERATIONS)


img = cv2.imread(IMG_PATH)
img = cv2.resize(img, (WIDTH, HEIGHT))
imgGrey = rgb2gray(img)

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

# TWORZENIE SINOGRAMU
for rays in structBuilder.rays:
    # wersja 1
    # sinogram.append(structBuilder.getMeanFromRays(rays, imgGrey))

    # wersja 2
    sinogram.append(structBuilder.getRaysMean(rays, imgGrey))

# DO WYSWIETLENIA SINOGRAMU
h = ITERATIONS
w = DETECTORS
new_img = np.zeros([h, w, 3], dtype=np.uint8)
new_img = rgb2gray(new_img)


# WYŚWIETLANIE / RYSOWANIE
i1=0
for rays in structBuilder.rays:
    img = np.copy(imgOrigin)

    if len(rays) <= 20:
        for ray in rays:
            for pixel in ray.pixels:
                cv2.circle(img, (int(pixel.x), int(pixel.y)), 1, (0, 255, 0), -1)
    else:
        for i in range (0,20):
            for pixel in rays[i*(int)(len(rays)/20)].pixels:
                cv2.circle(img, (int(pixel.x), int(pixel.y)), 1, (0, 255, 0), -1)

    for j in range(0,w):
        new_img[i1][j] = sinogram[i1][j]

    cv2.imshow('Sinogram', new_img)

    cv2.imshow('Tomograf', img)
    cv2.waitKey(1)
    i1+=1


new_img = cv2.resize(new_img, (w*4, h*4))
cv2.imshow('Sinogram', new_img)

cv2.imshow('Tomograf', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

