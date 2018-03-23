import cv2
from skimage.color import rgb2gray

from src import Settings
from src.Display import DisplayImages
from src.ImageProcessing import PProcessing
from src.StructBuilder import StructBuilder
import time
import numpy as np
from tkinter import *

WIDTH = 400
HEIGHT = 400
RADIUS = 200
DETECTORS = 40
DELTHA_ANGLE = 12
DETECTORS_WIDTH = 90
ITERATIONS = 60
IMG_PATH = './res/image_04.png'

#zmiana dokladnosci punktów. np. dla accuracy = 2 -> 1 stopien = 1/2 stopnia
# -> zamiast 360, 720 punktów okręgu
ACCURACY = 4


# settings = Settings.Settings(DETECTORS, DELTHA_ANGLE, DETECTORS_WIDTH, ITERATIONS, ACCURACY)

def start():
    imgProc = PProcessing()
    structBuilder = StructBuilder(WIDTH, HEIGHT, deltha.get()*ACCURACY, detectors.get(),
                                  d_width.get(), ACCURACY, iterations.get(), RADIUS)
    displayImages = DisplayImages(entry.get(), imgProc, structBuilder, WIDTH, HEIGHT,
                                  iterations.get(), detectors.get())

    displayImages.showImages()


def addLabel(text):
    var = StringVar()
    label = Label(window, textvariable=var, relief=RAISED)
    var.set(text)
    return label

def close():
    exit()

window = Tk()

entry = Entry(window, bd =5)
entry.insert(END, IMG_PATH)
entry.pack()

detectors = Scale(window, from_=2, to=200, length=800, orient=HORIZONTAL)
detectors.set(DETECTORS)
detectors.pack()
addLabel("Detectors").pack()

deltha = Scale(window, from_=1, to=359, length=800, orient=HORIZONTAL)
deltha.set(DELTHA_ANGLE)
deltha.pack()
addLabel("Deltha").pack()

d_width = Scale(window, from_=1, to=359, length=800, orient=HORIZONTAL)
d_width.set(DETECTORS_WIDTH)
d_width.pack()
addLabel("Detectors Width").pack()

iterations = Scale(window, from_=30, to=500, length=800, orient=HORIZONTAL)
iterations.set(ITERATIONS)
iterations.pack()
addLabel("Iterations").pack()

addLabel(" ").pack()

button = Button(window, text="Start", command=start)
button.pack()

window.mainloop()

