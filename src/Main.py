from src import ImageProcessing
from src import Display
from src import StructBuilder
from tkinter import *

WIDTH = 400                         # wymiary wyjściowego obrazka
HEIGHT = 400                        # - || -
RADIUS = 200                        # promień rysowanego okręgu
DETECTORS = 40                      # liczba detektorów
DELTHA_ANGLE = 6                   # kąt przmieszczenia generatora w każdej iteracji
DETECTORS_WIDTH = 90                # rozpiętość łuku, na którym znajdują się detektory
ITERATIONS = 60                     # liczba obrotów generatora
IMG_PATH = './res/image_04.png'     # lokalizacja zdjęcia
ACCURACY = 4                        # jak gęsto tworzyć punkty dla okręgu


def start():
    #Do tworzenia pixeli i odcinków algorytmem Bresenhama
    imgProc = ImageProcessing.PProcessing()

    #Tworzenie okręgu i tablicy promieni z każdej iteracji (ogólnie zbieranie informacji)
    structBuilder = StructBuilder.StructBuilder(WIDTH, HEIGHT, deltha.get()*ACCURACY, detectors.get(),
                                  d_width.get(), ACCURACY, iterations.get(), RADIUS)

    #Wyświetlanie obrazków, tworzenie sinogramu i odwzorowanie oryginalnego obrazka
    displayImages = Display.DisplayImages(entry.get(), imgProc, structBuilder, WIDTH, HEIGHT,
                                  iterations.get(), detectors.get())

    displayImages.showImages()


#Dalej tylko UI
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

