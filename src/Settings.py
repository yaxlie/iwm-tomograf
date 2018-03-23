import cv2
from tkinter import *

class Settings:
    def __init__(self, detectors, deltha_angle, detectors_width, iterations, accuracy):

        self.detectors = detectors
        self.deltha_angle = deltha_angle
        self.detectors_width = detectors_width
        self.iterations = iterations


        def onDetectorsChange(x):
            p = cv2.getTrackbarPos('Detectors', 'Settings')
            self.detectors = p

            pass
        def onDelthaChange(x):
            p = cv2.getTrackbarPos('Deltha', 'Settings')
            self.deltha_angle = p*accuracy
            pass

        def onDWidthChange(x):
            p = cv2.getTrackbarPos('Detectors Width', 'Settings')
            self.detectors_width = p*accuracy
            pass

        def onIterChange(x):
            p = cv2.getTrackbarPos('Iterations', 'Settings')
            self.iterations = p
            pass

        cv2.namedWindow('Settings', cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Settings", 300, 200)

        cv2.createTrackbar('Detectors', 'Settings', 2, 200, onDetectorsChange)
        cv2.createTrackbar('Deltha', 'Settings', 1, 359, onDelthaChange)
        cv2.createTrackbar('Detectors Width', 'Settings', 1, 359, onDWidthChange)
        cv2.createTrackbar('Iterations', 'Settings', 0, 1000, onIterChange)

        cv2.setTrackbarPos('Detectors', 'Settings', detectors)
        cv2.setTrackbarPos('Deltha', 'Settings', deltha_angle)
        cv2.setTrackbarPos('Detectors Width', 'Settings', detectors_width)
        cv2.setTrackbarPos('Iterations', 'Settings', iterations)

        cv2.moveWindow("Settings", 0, 0)
        cv2.waitKey(0)
        pass
