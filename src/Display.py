import cv2
from skimage.color import rgb2gray

from src.ImageProcessing import PProcessing
from src.StructBuilder import StructBuilder
import time
import numpy as np

SCALING = 6
RIGHT_SHIFT = 350

class DisplayImages:

    def __init__(self, imgPath, imgProc, structBuilder, width, height, iterations, detectors):
        self.imgPath = imgPath
        self.imgProc = imgProc
        self.structBuilder = structBuilder
        self.width = width
        self.height = height
        self.iterations = iterations
        self.detectors = detectors

    def showImages(self):
        img = cv2.imread(self.imgPath)
        img = cv2.resize(img, (self.height, self.width))
        imgGrey = rgb2gray(img)

        for o in self.structBuilder.circle:
            cv2.circle(img, (int(o.x), int(o.y)), 2, (0, 0, 255), -1)


        imgOrigin = np.copy(img)

        self.structBuilder.createRays()

        # TWORZENIE SINOGRAMU
        sinogram = []
        for rays in self.structBuilder.rays:
            sinogram.append(self.structBuilder.getRaysMean(rays, imgGrey))

        # DO WYSWIETLENIA SINOGRAMU
        h = self.iterations
        w = self.detectors
        new_img = np.zeros([h, w, 3], dtype=np.uint8)
        new_img = rgb2gray(new_img)

        cv2.imshow('Tomograf', img)
        cv2.imshow('Sinogram', new_img)
        cv2.moveWindow('Tomograf', RIGHT_SHIFT, 0)
        cv2.moveWindow('Sinogram', self.width + 50 + RIGHT_SHIFT, 0)

        # WYŚWIETLANIE / RYSOWANIE
        i1 = 0
        for rays in self.structBuilder.rays:
            img = np.copy(imgOrigin)

            if len(rays) <= 20:
                for ray in rays:
                    for pixel in ray.pixels:
                        cv2.circle(img, (int(pixel.x), int(pixel.y)), 1, (0, 255, 0), -1)
            else:
                for i in range(0, 20):
                    for pixel in rays[i * (int)(len(rays) / 20)].pixels:
                        cv2.circle(img, (int(pixel.x), int(pixel.y)), 1, (0, 255, 0), -1)

            for j in range(0, w):
                new_img[i1][j] = sinogram[i1][j]

            cv2.imshow('Sinogram', new_img)
            cv2.imshow('Tomograf', img)
            cv2.waitKey(1)
            i1 += 1

        new_img = cv2.resize(new_img, (w * SCALING, h * SCALING))
        cv2.imshow('SinogramZoom', new_img)

        cv2.imshow('Tomograf', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()