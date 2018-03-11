import cv2
import numpy as np
from ImageProcessing import Pixel
from ImageProcessing import PProcessing

RADIUS = 200
ITERATIONS = 50

class StructBuilder:
    def __init__(self, width, height, delta_detectors, detectors, detectors_width):
        self.width = width
        self.height = height
        self.delta_detectors = delta_detectors
        self.detectors = detectors
        self.detectors_width = detectors_width
        self.rays = []
        self.iterations = ITERATIONS
        self.circle = self.pointsInCircum(RADIUS, 360)
        pass

    def pointsInCircum(self, r, n=100):
        return [Pixel(np.math.cos(2 * np.pi / n * x) * r + self.width / 2,
                      np.math.sin(2 * np.pi / n * x) * r + self.height / 2)
                for x in range(0, n + 1)]

    def createRays(self):
        processing = PProcessing()
        for i in range(0,self.iterations):
            self.rays.append(processing.bresenhamLine(
                self.circle[i].x, self.circle[i].y,self.circle[i+180].x, self.circle[i+180].y))

