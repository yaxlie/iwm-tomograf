import cv2
import numpy as np
from ImageProcessing import Pixel
from ImageProcessing import PProcessing

RADIUS = 200
ITERATIONS = 200

class Ray:
    def __init__(self, startPixel, endPixel):
        processing = PProcessing()
        self.pixels = processing.bresenhamLine(
                int(startPixel.x), int(startPixel.y), int(endPixel.x), int(endPixel.y))

class StructBuilder:
    def __init__(self, width, height, deltha_angle, detectors, detectors_width):
        self.width = width
        self.height = height
        self.deltha_angle = deltha_angle
        self.detectors = detectors
        self.detectors_width = detectors_width
        self.rays = []
        self.iterations = ITERATIONS

        if self.detectors < 2:
            self.detectors = 2

        self.circle = self.pointsInCircum(RADIUS, 360)
        pass

    def pointsInCircum(self, r, n=100):
        return [Pixel(np.math.cos(2 * np.pi / n * x) * r + self.width / 2,
                      np.math.sin(2 * np.pi / n * x) * r + self.height / 2)
                for x in range(0, n + 1)]

    def createRays(self):
        for i in range(0,self.iterations):
            list = []
            startAngle = i*int(self.deltha_angle)
            startPixel = self.circle[startAngle%360]

            startWidth = startAngle + 180 + int(self.detectors_width/2)
            for j in range(0,self.detectors):
                list.append(Ray(startPixel,
                                self.circle[(startWidth - j * 2 * int(self.detectors_width / self.detectors))%360]))
            self.rays.append(list)

    def getMeanFromRay(self, ray, img):
        colorList = []
        for r in ray:
            list = []
            for pixel in r.pixels:
                list.append(img[pixel.x-1][pixel.y-1])
            colorList.append(list)
        return [float(sum(col))/len(col) for col in zip(*colorList)]





