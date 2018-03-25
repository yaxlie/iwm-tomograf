import numpy as np
from src.ImageProcessing import Pixel
from src.ImageProcessing import PProcessing

class Ray:
    def __init__(self, startPixel, endPixel):
        processing = PProcessing()
        self.pixels = processing.bresenhamLine(
                int(startPixel.x), int(startPixel.y), int(endPixel.x), int(endPixel.y))

class StructBuilder:
    def __init__(self, width, height, deltha_angle, detectors,
                 detectors_width, accuracy, iterations, radius):
        self.width = width
        self.height = height
        self.deltha_angle = deltha_angle * accuracy
        self.detectors = detectors
        self.detectors_width = detectors_width * accuracy
        self.rays = []
        self.iterations = iterations
        self.accuracy = accuracy

        if self.detectors < 2:
            self.detectors = 2

        self.circle = self.pointsInCircum(radius, 360 * accuracy)
        pass

    #tworzenie okręgu
    def pointsInCircum(self, r, n=100):
        return [Pixel(np.math.cos(2 * np.pi / n * x) * r + self.width / 2,
                      np.math.sin(2 * np.pi / n * x) * r + self.height / 2)
                for x in range(0, n + 1)]

#tworzy wszystkie promienie z wszystkich iteracji
    def createRays(self):
        for i in range(0,self.iterations):
            list = []
            startAngle = i*int(self.deltha_angle)
            startPixel = self.circle[startAngle%(360*self.accuracy)]

            startWidth = startAngle + 180 * self.accuracy + int(self.detectors_width/2)
            endWidth = startAngle + 180 * self.accuracy - int(self.detectors_width / 2)
            d = (startWidth - endWidth)/(self.detectors-1)

            for j in range(0,self.detectors):
                list.append(Ray(startPixel,
                                self.circle[int(startWidth - j * d)%(360*self.accuracy)]))
            self.rays.append(list)

# Zwraca piksele pojedyńczej iteracji (detektory)
    def getRaysMean(self, rays, img):
        colorList = []
        for r in rays:
            list = []
            for pixel in r.pixels:
                list.append(img[pixel.x-1][pixel.y-1])
            colorList.append(sum(list) / float(len(list)))
        return colorList




