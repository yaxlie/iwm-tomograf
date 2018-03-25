import cv2
from skimage.color import rgb2gray

from src.ImageProcessing import PProcessing
from src.StructBuilder import StructBuilder
import time
import numpy as np

SCALING = 4
RIGHT_SHIFT = 350
TOP_SHIFT = 400

class DisplayImages:

    def __init__(self, imgPath, imgProc, structBuilder, width, height, iterations, detectors):
        self.imgPath = imgPath
        self.imgProc = imgProc
        self.structBuilder = structBuilder
        self.width = width
        self.height = height
        self.iterations = iterations
        self.detectors = detectors
        self.sinogram = None
        self.revertedImage = None

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
        self.sinogram = np.copy(new_img)

        cv2.imshow('Tomograf', img)

        self.revertImage()

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def revertImage(self):
        img = self.sinogram
        img = rezise_image(img, max(img.shape), max(img.shape))

        # img = self.get_one_image([np.copy(zeros), img])
        # dst = self.get_one_image([np.copy(img), np.copy(zeros)])
        # tmp = self.get_one_image([np.copy(img), np.copy(zeros)])

        dst = np.copy(img)
        tmp = np.copy(img)
        x = None

        cv2.imshow('Reversion', img)
        cv2.moveWindow('Reversion', RIGHT_SHIFT, TOP_SHIFT)

        for i in range(2,60):
            rows, cols = np.copy(img).shape
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 12, 1)
            # dst = cv2.warpAffine(img, M, (cols, rows))
            tmp = cv2.warpAffine(tmp, M, (cols,  rows))
            # dst = 0.5 * tmp

            x = dst + tmp
            # print(np.amax(x), x[1][1])
            cv2.imshow('Reversion', x)
            # time.sleep(1)
            cv2.waitKey(1)
            dst = np.copy(x)

        self.revertedImage = dst
        cv2.imshow('Reversion', (x/60) / np.amax(x/60))
        # time.sleep(1)
        cv2.waitKey(1)


def rezise_image(img, w, h):
    height, width = img.shape
    x = w - width
    y = h - height

    i = 0
    while i < x:
        img = cv2.copyMakeBorder(img, 0, 0, 1, 0, cv2.BORDER_CONSTANT)
        i+=1
        if i < x:
            img = cv2.copyMakeBorder(img, 0, 0, 0, 1, cv2.BORDER_CONSTANT)
            i += 1
    i = 0
    while i < y:
        img = cv2.copyMakeBorder(img, 1, 0, 0, 0, cv2.BORDER_CONSTANT)
        i += 1
        if i < y:
            img = cv2.copyMakeBorder(img, 0, 1, 0, 0, cv2.BORDER_CONSTANT)
            i += 1

    return img